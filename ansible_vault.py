import sublime, os, sublime_plugin

class AnsibleVaultCommand(sublime_plugin.WindowCommand):
    def is_vaulted_file(self):
        marker = sublime.Region(0, 14)
        start  = self.window.active_view().substr(marker)
        return start == '$ANSIBLE_VAULT'

    def working_dir(self):
        return self.window.folders()[0]

    def working_file(self):
        return self.window.active_view().file_name()

    def build_command(self, mode):
        result = ("cd " + self.working_dir() +
                  " && ansible-vault " + mode +
                  " " + self.working_file())
        return result

    def execute_command(self, mode):
        os.system(self.build_command(mode))

class AnsibleVaultToggleCommand(AnsibleVaultCommand):
    def run(self, paths=[], parameters=None):
        mode = 'decrypt' if self.is_vaulted_file() else 'encrypt'
        self.execute_command(mode)

class AnsibleVaultEncryptCommand(AnsibleVaultCommand):
    def run(self, paths=[], parameters=None):
        self.execute_command('encrypt')

class AnsibleVaultDecryptCommand(AnsibleVaultCommand):
    def run(self, paths=[], parameters=None):
        self.execute_command('decrypt')

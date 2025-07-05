from abc import ABC, abstractmethod


class Plugin(ABC):
    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def unload(self):
        pass


class SpellCheckPlugin(Plugin):
    def load(self):
        print("SpellCheckPlugin: Đang tải plugin kiểm tra chính tả...")

    def execute(self):
        print("SpellCheckPlugin: Đã kiểm tra chính tả cho văn bản.")

    def unload(self):
        print("SpellCheckPlugin: Gỡ plugin kiểm tra chính tả.")

class AutoSavePlugin(Plugin):
    def load(self):
        print("AutoSavePlugin: Đang tải plugin tự động lưu...")

    def execute(self):
        print("AutoSavePlugin: Đã tự động lưu văn bản.")

    def unload(self):
        print("AutoSavePlugin: Gỡ plugin tự động lưu.")

class PluginManager:
    def __init__(self):
        self.plugins = []

    def register_plugin(self, plugin):
        if isinstance(plugin, Plugin):
            self.plugins.append(plugin)
            print(f"Đã đăng ký plugin: {plugin.__class__.__name__}")
        else:
            print("Plugin không hợp lệ!")

    def run_all(self):
        for plugin in self.plugins:
            print(f"\n--- Thực thi plugin: {plugin.__class__.__name__} ---")
            plugin.load()
            plugin.execute()
            plugin.unload()

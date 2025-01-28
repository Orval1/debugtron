class PluginBase:
    """
    Base class for all plugins.
    """

    def __init__(self, name):
        """
        Initialize the plugin with a name.

        :param name: Name of the plugin.
        """
        self.name = name

    def execute(self, **kwargs):
        """
        Abstract method to execute the plugin's functionality.

        :param kwargs: Arguments needed for plugin execution.
        :return: Result of the plugin execution.
        """
        raise NotImplementedError("Plugins must implement the 'execute' method.")

    def __repr__(self):
        return f"<Plugin: {self.name}>"

# Example usage of PluginBase (can be extended by other plugins)
if __name__ == "__main__":
    class SamplePlugin(PluginBase):
        def execute(self, **kwargs):
            return f"Executing {self.name} with {kwargs}"

    sample_plugin = SamplePlugin(name="SamplePlugin")
    print(sample_plugin.execute(param="test"))

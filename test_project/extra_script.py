Import("env")
from SCons.Script import AddOption, GetOption

AddOption("--foo", dest="foo", action="store", default="default_foo")
AddOption("--enable-feature", dest="feature", action="store_true", default=False)
AddOption("--retry-count", dest="retry_count", type="int", action="store", default=3)

print("--- CUSTOM ARGUMENT PARSING RESULTS ---")
print("foo         :", GetOption("foo"))
print("feature     :", GetOption("feature"))
print("retry_count :", GetOption("retry_count"))
print("---------------------------------------")

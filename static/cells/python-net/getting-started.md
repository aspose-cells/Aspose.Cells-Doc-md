##Getting Started
Learn how to install Aspose.Cells for Python via .NET and create Hello World Application.
## **System Requirements**
Aspose.Cells for Python via .NET is platform-independent API and can be used on any platform (Windows and Linux) where [Python](https://www.python.org/downloads/) is installed.
## **Python Version**
- Python 3.6 or higher
## **Installation**
### **Windows:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
$ pip install aspose-cells-python
### **Linux:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
$ pip install aspose-cells-python
- Note:You need to run the following command before installation
For Ubuntu/Debian: apt-get install libgdiplus
For CentOS/RHEL/Fedora: yum install libgdiplus
### **MacOS:**
You can easily use Aspose.Cells for Python via .NET from [pypi](https://pypi.org/project/aspose-cells-python/) with the following command.
$ pip install aspose-cells-python
- Note:If your python is Python3.7(take python3.7, for example, here),after installing the aspose-cells-python,there may be the following errors
'/usr/local/lib/libpython3.7m.dylib' (no such file), '/usr/lib/libpython3.7m.dylib' (no such file) prompt.
In such a situation,please add the following command to your bash_profile(Find where is libpython3.7m.dylib first,take /Library/Frameworks/Python.framework/Versions/3.7/lib
for example here)
export DYLD_LIBRARY_PATH="$DYLD_LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib"
export LIBRARY_PATH="$LIBRARY_PATH:/Library/Frameworks/Python.framework/Versions/3.7/lib/"
- Note:Due to our reliance on the SkiaSharp graphics library, if you encounter the following error:
**System.DllNotFoundException: Unable to load shared library 'libSkiaSharp' or one of its dependencies.** please install SkiaSharp.
brew  install nuget
nuget install SkiaSharp.NativeAssets.macOS -Version 2.88.6
After installation, please run the following command
cp ./SkiaSharp.NativeAssets.macOS.2.88.6/runtimes/osx/native/libSkiaSharp.dylib /usr/local/lib/.
Of course, if you want it simpler, you can also download [libSkiaSharp.dylib](libSkiaSharp.dylib) and then **copy** it to the **/usr/local/lib** directory.
> ⚠️ **Note:**
In some cases, after installing a new version of **aspose-cells-python**, users may encounter an error like the following:
**While initializing the host for the ‘WrpNs_Aspose.WrpNs_Cells.WrpCs_Workbook_xxxxxx (Assembly=WrpInterop.Aspose.Cells)’ type, an error occurred - Method ‘call_000_xxxxxx’ not found**
This indicates that the previous version was not completely uninstalled, leading to a conflict between the newly installed version and the old one.
You can resolve this issue by following the steps below:
- First, you can create a clean virtual environment to ensure the latest version works properly on your Windows machine:
```
# Set up virtual environment
python -m venv .venv
.\.venv\Scripts\activate
# Install aspose-cells-python
pip install aspose-cells-python
```
Then run your program.
- If you prefer to continue using your original environment, please try the following steps:
```
pip uninstall aspose-cells-python
```
Make sure the uninstallation is successful. If any errors occur during uninstallation, try running the command multiple times.
Alternatively, locate your **site-packages** directory, typically something like:
```
\Python3x\Lib\site-packages
```
Then manually delete the following directories (if they exist):
```
aspose
aspose_cells*
```
After that, reinstall the package:
```
pip install aspose-cells-python
```
## **How to Create the Hello World Application using Aspose.Cells for Python via .NET**
- Create a file named **CreatingHelloWorldFile.py** and use the following sample code:
- Now save the code above to "CreatingHelloWorldFile.py" and run "python CreatingHelloWorldFile.py" @command prompt.
## **Python via .NET Example github**
- Please visit the [Aspose.Cells for Python via .NET Example](https://github.com/aspose-cells/Aspose.Cells-for-Python-via-.NET) github to view more sample codes.

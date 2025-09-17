##custom localization
This article introduces how to customize localization in GridDesktop.
If we need to do localization for all the menus/message tips etc. in GridDesktop,We can define the resource file ,and use GridDesktop.SetCustomResourceManager to load this resource.
## **example**
first add a new resource file: customtest.resx
![custom-resource](managing-griddesktops-custom-res.png)
```csharp
//suppose your application with name space: myapp
ResourceManager rm = new ResourceManager("myapp.customtest", Assembly.GetExecutingAssembly());
gridDesktop1.SetCustomResourceManager(rm);
```
After executing the above code,   menu items shows:
![show menu](managing-griddesktops-show-custom.png)

##Use Your Own Icons Instead of the GridWeb Default Icons
This article describes how to use icons in GridWeb.
Sometimes you might want to use your own icons (images) instead of Aspose.Cells.GridWeb control's default icons. This article explains how to do this.
The control’s default icons are located in the URL path "/acw_client/". The file path can be: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" by default. You find files like submit.gif, save.gif etc. in that folder. If you want to replace these images with your own, add a config section to the web.config file of your web application.
**XML**
You may have noticed that this configuration only affects the control images path and doesn't affect the control’s client-scripts path. For example, if you run your page with the GridWeb control and check the source file in the browser, you may find that the acw_client _path property of the grid’s DIV element still says: “/yourApp/webform1.aspx/”. In some cases, you may need to redefine the client-script path. To force the control to use the redefined image path as the client-script path, add another config setting in the appSettings sectsection
**XML**
This config will only take effect with the licensed control.

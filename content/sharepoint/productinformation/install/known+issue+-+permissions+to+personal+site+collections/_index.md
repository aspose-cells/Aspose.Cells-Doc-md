---
title : "Known Issue - Permissions to Personal Site Collections" 
description : "" 
weight : 12019 
toc : false
type: docs
url: /sharepoint/productinformation/install/known+issue+-+permissions+to+personal+site+collections/
---

# Aspose.Cells for SharePoint : Known Issue - Permissions to Personal Site Collections


SharePoint by default does not grant full permissions to manage personal sites to portal administrators. That is why activation and deactivation on a personal site collection might fail when it is performed by portal administrators. This includes activation and deactivation during setup.

### Granting Permission to Personal Sites

When this issue occurs during installation, an `UnauthorizedAccessException` at `Microsoft.SharePoint.SPFeature.Activate()` is logged to the SharePoint trace log. When deactivation fails as a part of un-installation, an `UnauthorizedAccessException` is displayed on the last setup screen for the failed deactivation(s).

To prevent this issue, grant portal administrators the permission to manage MySite Web application:

1.  Go to **SharePoint Central Administration** and select the **Application Management** tab.
2.  Choose **Policy for Web Application** under the **Application Security** group.
3.  Make sure you select the correct Web Application for your “My Site” in the **Web Application** list on the right.
4.  Select **Add Users** on the upper left.
5.  Choose **All Zones** by default on the **Add Users** screen and click **Next**.
6.  Add the appropriate user(s) or active directory group that you want to have control over your “My Site” Web Application.
7.  Select the level of control.  
      
    **Adding users and setting the control level**  
    ![](https://docs2.aspose.com/cells/sharepoint/attachments/6356998/6488108.png)  
      
    
8.  Click **Finish**.

## Attachments:

![](https://docs2.aspose.com/cells/sharepoint/images/icons/bullet_blue.gif) [A known issue regarding permissions to the personal site collections-001.png](https://docs2.aspose.com/cells/sharepoint/attachments/6356998/6488108.png) (image/png)  


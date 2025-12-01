---
title: Known Issue - Permissions to Personal Site Collections
type: docs
weight: 40
url: /sharepoint/known-issue-permissions-to-personal-site-collections/
ai_search_scope: cells_sharepoint
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

SharePoint by default does not grant full permissions to manage personal sites to portal administrators. That is why activation and deactivation on a personal site collection might fail when it is performed by portal administrators. This includes activation and deactivation during setup.

{{% /alert %}} 
### **Granting Permission to Personal Sites**
When this issue occurs during installation, an UnauthorizedAccessException at Microsoft.SharePoint.SPFeature.Activate() is logged to the SharePoint trace log. When deactivation fails as a part of un-installation, an UnauthorizedAccessException is displayed on the last setup screen for the failed deactivation(s).

To prevent this issue, grant portal administrators the permission to manage MySite Web application:

1. Go to **SharePoint Central Administration** and select the **Application Management** tab.
1. Choose **Policy for Web Application** under the **Application Security** group.
1. Make sure you select the correct Web Application for your “My Site” in the **Web Application** list on the right.
1. Select **Add Users** on the upper left.
1. Choose **All Zones** by default on the **Add Users** screen and click **Next**.
1. Add the appropriate user(s) or active directory group that you want to have control over your “My Site” Web Application.
1. Select the level of control. 

   **Adding users and setting the control level** 

![todo:image_alt_text](known-issue-permissions-to-personal-site-collections_1.png)




1. Click **Finish**.

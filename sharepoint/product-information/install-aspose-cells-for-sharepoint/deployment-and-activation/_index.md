---
title: Deployment and Activation
type: docs
weight: 20
url: /sharepoint/deployment-and-activation/
---

{{% alert color="primary" %}} 

[Installing Aspose.Cells for SharePoint](/cells/sharepoint/installing-aspose-cells-for-sharepoint/) walks you through the installation process. This article explains what the installation process is deployed and activated.

{{% /alert %}} 
### **Deployment**
Aspose.Cells for SharePoint performs the following actions during deployment:

1. Installs **Aspose.Cells.SharePoint.dll** into the Global Assembly Cache and adds a SafeControl entry to the **web.config** file.
1. Installs feature manifest and other necessary files to the appropriate directories.
1. Registers the feature in the SharePoint database and makes it available for activation at the feature scope.
### **Activation**
Aspose.Cells for SharePoint is packaged as a site (site collection) level feature and can be activated and deactivated on site collections. 

During activation, the feature makes some changes to the virtual directory of the parent web application of the site collection:

1. Adds conversion settings page to the sitemap file.
1. Copies necessary resource files to the App_GlobalResources folder in the virtual directory.

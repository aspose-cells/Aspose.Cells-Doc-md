---
title: Uninstalling Aspose.Cells for SharePoint License
type: docs
weight: 30
url: /sharepoint/uninstalling-aspose-cells-for-sharepoint-license/
---

{{% alert color="primary" %}} 

To uninstall Aspose.Cells for SharePoint license, please use the steps below from the server console. 

{{% /alert %}} 

1. Retract the license solution from the farm:
   stsadm.exe -o retractsolution -name Aspose.Cells.SharePoint.License.wsp -immediate
1. Execute administrative timer jobs to complete the retraction immediately:
   stsadm.exe -o execadmsvcjobs
1. Wait for the retraction to complete.
   You can use Central Administration to check if the retraction has completed by going to **Central Administration**, then **Operations** and **Solution Management**.
1. Remove the solution from the SharePoint solution store:
   stsadm.exe -o deletesolution -name Aspose.Cells.SharePoint.License.wsp

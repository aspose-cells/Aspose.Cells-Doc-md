##Installing Aspose.Cells for SharePoint License
Once you are happy with your [evaluation](https://docs.aspose.com/cells/sharepoint/evaluate-aspose-cells/), [buy a license](https://purchase.aspose.com/buy).
Before buying, make sure that you understand and agree to the license subscription terms.
The license is emailed to you when the order has been paid. The license is a ZIP archive containing a regular SharePoint solution package.
The license ZIP contains:
- **Aspose.Cells.SharePoint.License.wsp** – SharePoint solution package file. The Aspose.Cells for SharePoint license is packaged as a SharePoint solution to facilitate deployment and retraction across the server farm.
- **readme.txt** – License installation instructions. License installation is performed from the server console via the **stsadm.exe**. The steps required to install the license are given below.
#### **Installing the License**
Paths are omitted for clarity. Add the actual path to **stsadm.exe** and/or solution file when executing the steps below.
1. Run stsadm to add the solution to the SharePoint solution store:
stsadm.exe -o addsolution -filename Aspose.Cells.SharePoint.License.wsp
1. Deploy the solution to all servers in the farm:
stsadm.exe -o deploysolution -name Aspose.Cells.SharePoint.License.wsp -immediate -force
1. Execute administrative timer jobs to complete the deployment immediately:
stsadm.exe -o execadmsvcjobs
You will receive a warning when running the deployment step if the Windows SharePoint Services Administration service has not been started. **Stsadm.exe** relies on this service and Windows SharePoint Timer Service to replicate solution data across the farm. If these services are not running on your server farm, you may need to deploy the license separately to each server.

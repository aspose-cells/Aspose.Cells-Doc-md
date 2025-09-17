##Opening Excel File without Open Save Cancel Dialog Box with C++
Learn how to open a Microsoft Excel file in a browser without showing the Open-Save-Cancel dialog box using Aspose.Cells for C++.
This document explains how to open a Microsoft Excel file in a browser without showing the Open-Save-Cancel dialog box.
It is to be noted here that the security restriction that does not allow direct download of a file is enforced by Microsoft (or other browser vendors), not by Aspose. It is imposed to block and restrict potentially harmful files from getting downloaded to local machines.
It is risky for the client’s local system to allow download without showing the Open-Save-Cancel dialog to prompt for download. There is no option or workaround available from Aspose as it will be a very big security risk.
## **Why a security risk?**
The following image shows the Open-Save-Cancel dialog box shown by Internet Explorer when trying to download a file.
|**The Open-Save-Cancel dialog**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
As explained above, allowing a file to open or run on your system without confirmation that you really want it to is a security risk. Some files contains viruses, and some site will try to download harmful files to your machine without prompting you. It is therefore not recommended that you allow file download without the download prompt so that users have to verify the file and its source can be verified before downloading or running it. Disabling the download dialog box makes the system vulnerable to viruses, Trojans and hackers who may silently affect your system.
## **Opening a File without the Open-Save-Cancel dialog box**
While it is a big security concern, Microsoft still provides Internet Explorer settings that allow users to disable the Open-Save-Cancel prompt for file download.
In Windows Explorer:
1. On the **Tools** menu, select **Folder Options**.
1. Click the File Types tab in the Folder Options dialog.
1. Select the XLS extension file type.
1. Click **Advanced**.
A dialog box is displayed. It has three options at the bottom.
1. Uncheck **Confirm open after download**.
1. Select the third option - **Browse in same window** - to view the Excel file in Internet Explorer without starting Microsoft Excel standalone.
|**Editing file type options**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
This setting allows files to run directly in the web browser, without the Open-Save-Cancel dialog showing when downloading or opening the file.

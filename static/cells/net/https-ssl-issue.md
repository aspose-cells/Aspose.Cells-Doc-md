##HTTPS SSL Issue
## **HTTPS/SSL Problem**
Some users reported that they had problems to download Excel files generated with Aspose.Cells. When the save dialog opens, the file name contains the name of the aspx page instead of the excel file, and the File Type is blank.
### **Explanation**
We changed HTTP response headers to solve the problem with HTTP compression. This may cause problem while sending files to client browser through HTTPS/SSL.
### **Solution**

##Licensing
## **Evaluation Version Limitations**
A free evaluation version of Aspose.Cells for Go via C++ can be downloaded from the downloads section of Aspose's web site at: <//<https://releases.aspose.com/cells/go-cpp/>>.
## **Loading a License from File**
When you call the SetLicense method, the license name that you pass should be that of the license file. For example, if you change the license file name to "Aspose.Cells.lic.xml" pass that file name to the License->SetLicense_String(…) method.
**Go**
lic, _:= NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))

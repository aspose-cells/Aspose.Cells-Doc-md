---
title: Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok
type: docs
weight: 130
url: /sv/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Möjliga användningsscenarier**

Aspose.Cells låter dig kopiera ett VBA-projekt från en Excel-fil till en annan Excel-fil. VBA-projektet består av olika typer av moduler t.ex. Document, Procedural, Designer, etc. Alla moduler kan kopieras med enkel kod men för Designer-modulen finns det lite extra data som kallas Designer Storage som behöver nås eller kopieras. Följande två metoder handlar om Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok**

Se följande exempelkod. Den kopierar VBA-projektet från[mall Excel-fil](50528345.xlsm) i en tom arbetsbok och sparar den som[utdata Excel-fil](50528346.xlsm). Om du öppnar VBA-projektet inuti mallen Excel-fil, kommer du att se ett användarformulär som visas nedan. Användarformuläret består av Designer Storage, så det kommer att kopieras med[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)och[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)metoder.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Följande skärmdump visar utdata Excel-filen och dess innehåll som kopierades från mallen Excel-fil. När du klickar på knappen 1 öppnas VBA User Form som i sig har en kommandoknapp som visar en meddelanderuta när du klickar.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}

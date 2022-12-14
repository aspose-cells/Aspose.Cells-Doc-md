---
title: Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok
type: docs
weight: 60
url: /sv/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---
## **Möjliga användningsscenarier**

Aspose.Cells låter dig kopiera VBA-projektet från en Excel-fil till en annan Excel-fil. VBA-projektet består av olika typer av moduler t.ex. Document, Procedural, Designer etc. Alla moduler kan kopieras med enkel kod men för Designer-modulen finns det lite extra data som kallas Designer Storage som måste nås eller kopieras. Följande två metoder handlar om Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String))
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[]))

## **Kopiera VBA Macro UserForm DesignerStorage från mall till målarbetsbok**

Se följande exempelkod. Den kopierar VBA-projektet från[mall Excel-fil](50528367.xlsm)i en tom arbetsbok och sparar den som[utdata Excel-fil](50528366.xlsm). Om du öppnar VBA-projektet inuti mallen Excel-fil, kommer du att se ett användarformulär som visas nedan. Användarformuläret består av Designer Storage, så det kommer att kopieras med[**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage(java.lang.String)) och[**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage(java.lang.String,%20byte[])) metoder.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

Följande skärmdump visar utdata Excel-filen och dess innehåll som kopierades från mallen Excel-fil. När du klickar på knappen 1 öppnas VBA User Form som i sig har en kommandoknapp som visar en meddelanderuta när du klickar.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}

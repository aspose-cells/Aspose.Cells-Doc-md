---
title: Kopiera VBA makro UserForm DesignerStorage från mallen till mål arbetsboken
type: docs
weight: 60
url: /sv/java/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells låter dig kopiera VBA-projektet från en Excel-fil till en annan Excel-fil. VBA-projektet består av olika typer av moduler, dvs. dokument, proceduriell, designer etc. Alla moduler kan kopieras med enkel kod, men för Designer-modulen finns det några extra data som kallas Designer Storage som måste nås eller kopieras. Följande två metoder hanterar Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-)

## **Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken**

Se följande exempelkod. Den kopierar VBA-projektet från [mall-excel-filen](50528367.xlsm) till en tom arbetsbok och sparar den som [output-excel-filen](50528366.xlsm). Om du öppnar VBA-projektet i mall-excel-filen kommer du att se ett Användarformulär som visas nedan. Användarformuläret består av Designer Storage, så det kommer att kopieras med [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#getDesignerStorage-java.lang.String-) och [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#addDesignerStorage-java.lang.String-byte[]-) metoder.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)

Följande skärmbild visar den genererade output-excel-filen och dess innehåll som kopierades från mall-excel-filen. När du klickar på Knapp 1 öppnar det VBA-användarformuläret som i sig har en kommandoknapp som visar en meddelanderuta när du klickar på den.

![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}

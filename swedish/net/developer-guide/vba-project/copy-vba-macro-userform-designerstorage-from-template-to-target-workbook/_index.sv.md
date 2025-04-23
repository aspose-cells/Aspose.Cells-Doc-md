---
title: Kopiera VBA makro UserForm DesignerStorage från mallen till mål arbetsboken
type: docs
weight: 130
url: /sv/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells låter dig kopiera ett VBA-projekt från en Excel-fil till en annan Excel-fil. VBA-projektet består av olika typer av moduler, t.ex. dokument-, procedural- och designarmoduler. Alla moduler kan kopieras med enkel kod, men för designermodulen finns det some extra data som kallas Designer Storage som behöver komma åt eller kopieras. De följande två metoderna hanterar Designer Storage.

- [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage)
- [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage)

## **Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken**

Se följande exempelkod. Den kopierar VBA-projektet från [mallens Excel-fil](50528345.xlsm) till en tom arbetsbok och sparar den som [utdata Excel-fil](50528346.xlsm). Om du öppnar VBA-projektet inne i mallens Excel-fil ser du en Användarformulär som visas nedan. Användarformuläret består av Designer Storage, så det kommer att kopieras med användning av [**VbaModuleCollection.GetDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/getdesignerstorage) och [**VbaModuleCollection.AddDesignerStorage()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/adddesignerstorage) metoder.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Följande skärmbild visar den utdata Excel-filen och dess innehåll som kopierades från mallens Excel-fil. När du klickar på knappen 1, öppnar den VBA Användarformuläret som i sig har en kommandoknapp som visar en meddelanderuta vid klick.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.cs" >}}
{{< app/cells/assistant language="csharp" >}}

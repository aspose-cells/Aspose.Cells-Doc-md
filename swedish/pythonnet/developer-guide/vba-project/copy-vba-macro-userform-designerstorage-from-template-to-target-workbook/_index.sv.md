---
title: Kopiera VBA makro UserForm DesignerStorage från mallen till mål arbetsboken
type: docs
weight: 130
url: /sv/python-net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/
---

## **Möjliga användningsscenario**

Aspose.Cells för Python via .NET tillåter dig att kopiera ett VBA-projekt från en Excel-fil till en annan. VBA-projekt består av olika typer av moduler, t.ex. Dokument, Procedural, Designer, etc. Alla moduler kan kopieras med enkel kod, men för Designer-modulen finns det extra data, kallad Designer Storage, som måste nås eller kopieras. Följande två metoder hanterar Designer Storage.

- [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str)
- [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage/)

## **Kopiera VBA-makro UserForm DesignerStorage från mallen till mål arbetsboken**

Se följande exempelkod. Den kopierar VBA-projektet från [mallens Excel-fil](50528345.xlsm) till en tom arbetsbok och sparar den som [utdata Excel-fil](50528346.xlsm). Om du öppnar VBA-projektet inne i mallens Excel-fil ser du en Användarformulär som visas nedan. Användarformuläret består av Designer Storage, så det kommer att kopieras med användning av [**VbaModuleCollection.get_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/get_designer_storage/#str) och [**VbaModuleCollection.add_designer_storage()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add_designer_storage) metoder.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_1.png)**

Följande skärmbild visar den utdata Excel-filen och dess innehåll som kopierades från mallens Excel-fil. När du klickar på knappen 1, öppnar den VBA Användarformuläret som i sig har en kommandoknapp som visar en meddelanderuta vid klick.

**![todo:image_alt_text](copy-vba-macro-userform-designerstorage-from-template-to-target-workbook_2.png)**

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CopyVBAMacroUserFormDesignerStorageToWorkbook.py" >}}


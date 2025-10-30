---
title: Ange maximala rader för delad formel
type: docs
weight: 40
url: /sv/python-net/specify-maximum-rows-of-shared-formula/
---

## **Möjliga användningsscenario**

Maximalt antal rader för delad formel är 64 som standard. Det kan vara vilket antal som helst, till exempel 1000. Prestandan för delad formel ändras beroende på antalet rader. Därför tillhandahåller Aspose.Cells för Python via .NET egenskapen [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) som kan användas för att ange max antal rader för den delade formeln. Den delade formeln delas upp i flera delade formler om det totala antalet rader överskrider detta, som visas i skärmkoppsbilden nedan.

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)

## **Ange maximala rader för delad formel**

Följande kodexempel förklarar användningen av [**Workbook.settings.max_rows_of_shared_formula**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/max_rows_of_shared_formula) egenskapen. Den sätter det maximala antalet rader för den delade formeln till 5 och lägger till den delade formeln i cellen D1 för 100 rader och sparar till [utmatnings-excelfil](61767856.xlsx). Om du extraherar innehållet i utmatnings-excelfilen och kontrollerar *sheet1.xml*, kommer du att se att den delade formeln delas upp efter varje 5 rader som markerat i den tidigare skärmbilden.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SpecifyMaximumRowsOfSharedFormula.py" >}}

{{< app/cells/assistant language="python-net" >}}

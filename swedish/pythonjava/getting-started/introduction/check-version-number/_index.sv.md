---
title: Kontrollera versionsnumret
type: docs
weight: 80
url: /sv/python-java/check-version-number/
---

{{% alert color="primary" %}}

Undrar vilken version av Aspose.Cells du använder? Vi publicerar nya versioner av Aspose.Cells, både för att introducera nya funktioner och för att åtgärda problem, regelbundet. Versionsnumret består av huvudversionsnummer, underversionsnummer och reparationversion. Varje nummer måste vara ett heltal från 0 och uppåt. Formatet är följande:

huvud.under.reparation

När vi släpper en ny version av Aspose.Cells uppdaterar vi versionsnumret.

Den här artikeln förklarar hur du kontrollerar vilken version av Aspose.Cells som är installerad på systemet manuellt och med hjälp av Aspose.Cells API.

{{% /alert %}}

## **Kontrollera versionsnummer manuellt**

För att manuellt ta reda på vilken version av Aspose.Cells du använder:

1. Högerklicka på filen Aspose.Cells.dll och välj **Egenskaper**.
1. Klicka på fliken Version (eller Detaljer) för att kontrollera versionsnumret.

## **Kontrollera versionsnummer med hjälp av Aspose.Cells API**

För att ta reda på vilken version av Aspose.Cells du använder genom API:et, använd klassen [CellsHelper](https://reference.aspose.com/cells/python-java/asposecells.api/cellshelper) för att hämta Aspose.Cells versionsnummer med hjälp av den statiska metoden GetVersion.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CheckVersionNumber.py" >}}

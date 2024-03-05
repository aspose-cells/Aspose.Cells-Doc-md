---
title: Kontrollera versionsnummer
type: docs
weight: 80
url: /sv/python-java/check-version-number/
---
{{% alert color="primary" %}}

Undrar vilken version av Aspose.Cells du använder? Vi publicerar nya versioner av Aspose.Cells, både för att introducera nya funktioner och för att åtgärda problem, regelbundet. Versionsnumret består av huvudversionsnummer, mindre versionsnummer och snabbkorrigeringsversionsnummer. Varje tal måste vara ett heltal från 0 uppåt. Formatet är som följer:

major.minor.snabbkorrigering

När vi släpper en ny version av Aspose.Cells uppdaterar vi versionsnumret.

Den här artikeln förklarar hur du kontrollerar vilken version av Aspose.Cells som är installerad på systemet manuellt och med Aspose.Cells API.

{{% /alert %}}

## **Kontrollera versionsnumret manuellt**

För att ta reda på vilken version av Aspose.Cells du använder manuellt:

1.  Högerklicka på filen Aspose.Cells.dll och välj**Egenskaper**.
1. Klicka på fliken Version (eller Detaljer) för att kontrollera versionsnumret.

## **Kontrollera versionsnummer med Aspose.Cells API**

 För att ta reda på vilken version av Aspose.Cells du använder via API, använd[CellsHelper](https://reference.aspose.com/cells/python-java/asposecells.api/cellshelper) klass GetVersion statisk metod för att få Aspose.Cells versionsnummer.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "CheckVersionNumber.py" >}}

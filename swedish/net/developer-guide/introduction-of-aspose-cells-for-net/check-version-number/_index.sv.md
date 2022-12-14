---
title: Kontrollera versionsnummer
type: docs
weight: 80
url: /sv/net/check-version-number/
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

 För att ta reda på vilken version av Aspose.Cells du använder via API:t, använd[CellsHelper](https://reference.aspose.com/cells/net/aspose.cells/cellshelper) klass GetVersion statisk metod för att få Aspose.Cells versionsnummer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}

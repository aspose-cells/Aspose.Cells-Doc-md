---
title: Kontrollera versionsnumret
type: docs
weight: 80
url: /sv/net/check-version-number/
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

För att ta reda på vilken version av Aspose.Cells du använder genom API:et, använd [CellsHelper](https://reference.aspose.com/cells/net/aspose.cells/cellshelper) klassens GetVersion statiska metod för att hämta Aspose.Cell's versionsnummer.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-CheckVersionNumber-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

---
title: Uppdatera och beräkna pivottabell med beräknade poster
type: docs
weight: 40
url: /sv/nodejs-cpp/refresh-and-calculate-pivot-table-having-calculated-items/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ stöder nu att uppdatera och beräkna pivottabeller med beräknade objekt. Använd [**PivotTable.refreshData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#refreshdata--) och [**PivotTable.calculateData**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#calculatedata--) som vanligt för att utföra denna funktion.

{{% /alert %}}

## **Uppdatera och beräkna pivottabell med beräknade poster**

Följande exempel kod laddar den [käll-Excel-filen](5115238.xlsx) som innehåller en pivottabell med tre beräknade objekt som "add", "div" och "div2". Vi ändrar först värdet i cell D2 till 20 och sedan uppdaterar och beräknar pivottabellen med hjälp av Aspose.Cells for Node.js via C++ API:er och sparar arbetsboken i PDF-format. Resultatet i [utdata-PDF](5115229.pdf) visar att Aspose.Cells for Node.js via C++ uppdaterade och beräknade pivottabellen med beräknade objekt framgångsrikt. Du kan verifiera det genom att manuellt sätta värdet 20 i cell D2 och sedan uppdatera pivottabellen med kortkommandot Alt+F5 eller klicka på pivottabellens Uppdatera-knapp.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTable-RefreshAndCalculateItems-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}

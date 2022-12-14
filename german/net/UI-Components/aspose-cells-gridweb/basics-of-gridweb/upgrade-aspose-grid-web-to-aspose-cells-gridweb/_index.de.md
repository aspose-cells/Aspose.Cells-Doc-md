---
title: Aktualisieren Sie Aspose.Grid.Web auf Aspose.Cells.GridWeb
type: docs
weight: 30
url: /de/net/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
---
{{% alert color="primary" %}}

Um das Upgrade zu vereinfachen, pflegen wir ein Dokument, das wichtige Informationen für bestehende Benutzer beschreibt, insbesondere für diejenigen, die das ältere Aspose.Grid.Web verwendet haben und auf das zusammengeführte Aspose.Cells.GridWeb aktualisieren müssen.

 Diese sind als kurze Notizen gedacht, und Sie sollten in der Lage sein, weitere Informationen zu finden, indem Sie sich die Abschnitte des ansehen[Entwicklerhandbuch](/cells/de/net/developer-guide/).

{{% /alert %}}

## **Upgrade auf Aspose.Cells.GridWeb**

 Benutzer von Aspose.Grid.Web können bei der Verwendung des neuen Aspose.Cells.GridWeb auf Probleme stoßen, wenn sie darauf aktualisieren. Es ist zu beachten, dass Aspose.Grid.Web umbenannt wurde und ein Teil von Aspose.Cells geworden ist, sodass wir ältere Versionen des Steuerelements nicht fortsetzen oder Änderungen daran vornehmen werden.

Es ist nicht schwer, auf die neueste Aspose.Cells.GridWeb-Komponente zu aktualisieren.

{{% alert color="primary" %}}

In der API gibt es ein paar Änderungen, da die Klassen mit den Membern, Structs, Enumerations etc. gleich bleiben. Die meisten Änderungen wurden an den Namespaces und anderen Tags oder Attributen des Steuerelements vorgenommen.

{{% /alert %}}

Das Folgende ist die Namensraumliste und andere Attribute/Tags, die jetzt geändert werden:

1. Der Namespace Aspose.Grid.Web wurde in Aspose.Cells.GridWeb umbenannt.
1. Der Namespace Aspose.Grid.Web.Data wurde in Aspose.Cells.GridWeb.Data umbenannt.
1. Der Namespace Aspose.Grid.Web.Design wurde in Aspose.Cells.GridWeb.Design umbenannt.
1. Der Namespace Aspose.Grid.Formula wurde in Aspose.Cells.GridFormula umbenannt, und mit den letzten Versionen der Komponente wurde der Namespace vollständig aus dem öffentlichen API entfernt.
1. Das Tag agw:GridWeb wurde in acw:GridWeb im Aspx-Format geändert.
1. Der ältere Clientpfad Aspose.Grid.Web, agw_client, hat sich zu acw geändert_Client für Aspose.Cells.GridWeb .
1.  Die Client-Pfadeinstellung in der Datei web.config, zum Beispiel:

{{< highlight "java" >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

 hat sich geändert zu

{{< highlight "java" >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

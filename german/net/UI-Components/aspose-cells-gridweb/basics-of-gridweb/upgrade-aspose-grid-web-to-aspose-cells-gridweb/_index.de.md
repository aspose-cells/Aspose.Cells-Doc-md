---
title: Aspose.Grid.Web zu Aspose.Cells.GridWeb aktualisieren
type: docs
weight: 30
url: /de/net/aspose-cells-gridweb/upgrade-aspose-grid-web-to-aspose-cells-gridweb/
keywords: GridWeb 
description: Dieser Artikel beschreibt, wie man in GridWeb aktualisiert.
---

{{% alert color="primary" %}}

Um das Upgrade zu erleichtern, führen wir eine Dokumentation, die für bestehende Benutzer, insbesondere solche, die das ältere Aspose.Grid.Web verwendet haben und auf das Aspose.Cells.GridWeb upgraden müssen, kritische Informationen enthält.

Diese sollen kurze Hinweise sein, und Sie sollten mehr Informationen finden, indem Sie die Abschnitte des [Entwicklerhandbuchs](/cells/de/net/aspose-cells-gridweb/developer-guide/) betrachten.

{{% /alert %}}

## **Upgrade auf Aspose.Cells.GridWeb**

Aspose.Grid.Web-Benutzer könnten beim Upgrade auf das neue Aspose.Cells.GridWeb auf Probleme stoßen. Es ist zu beachten, dass Aspose.Grid.Web umbenannt und ein Teil von Aspose.Cells geworden ist, daher werden wir ältere Versionen des Steuerelements nicht weiterführen oder ändern. 

Es ist nicht schwer, auf das neueste Aspose.Cells.GridWeb-Komponente zu aktualisieren.

{{% alert color="primary" %}}

Es gibt einige Änderungen in der API, da die Klassen mit den Membern, Strukturen, Aufzählungen usw. gleich bleiben. Die meisten Änderungen wurden an den Namensräumen des Steuerlements und anderen Tags oder Attributen vorgenommen.

{{% /alert %}}

Im Folgenden finden Sie die Liste der Namensräume und anderer Attribute/Tags, die jetzt geändert sind:

1. Der Aspose.Grid.Web-Namespace wurde in Aspose.Cells.GridWeb umbenannt.
1. Der Aspose.Grid.Web.Data-Namespace wurde in Aspose.Cells.GridWeb.Data umbenannt.
1. Der Aspose.Grid.Web.Design-Namespace wurde in Aspose.Cells.GridWeb.Design umbenannt.
1. Der Aspose.Grid.Formula-Namespace wurde in Aspose.Cells.GridFormula umbenannt und bei den neueren Versionen des Steuerlements wurde dieser Namespace vollständig aus der öffentlichen API entfernt.
1. Das Tag agw:GridWeb wurde in acw:GridWeb im aspx-Formular geändert.
1. Der ältere Aspose.Grid.Web-Clientpfad, agw_client, hat sich für Aspose.Cells.GridWeb zu acw_client geändert.
1. Die Clientpfad-Einstellung in der web.config-Datei, zum Beispiel: 

{{< highlight java >}}

 <appSettings> 

    <add key="aspose.grid.web.agw_client_path" value="/agw_client/" />

    <add key="aspose.grid.web.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

hat sich geändert zu 

{{< highlight java >}}

 <appSettings>

    <add key="aspose.cells.gridweb.acw_client_path" value="/acw_client/" />

    <add key="aspose.cells.gridweb.force_script_path" value="true" />

</appSettings>



{{< /highlight >}}

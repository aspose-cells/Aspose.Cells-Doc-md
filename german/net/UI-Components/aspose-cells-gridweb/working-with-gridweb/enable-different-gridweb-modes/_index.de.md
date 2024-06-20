---
title: Verschiedene GridWeb Modi aktivieren
type: docs
weight: 60
url: /de/net/aspose-cells-gridweb/enable-different-gridweb-modes/
keywords: GridWeb,EditMode,SessionMode
description: Dieser Artikel zeigt, wie man mit dem Bearbeitungsmodus und dem Sitzungsmodus in GridWeb arbeitet.
---

{{% alert color="primary" %}} 

In diesem Artikel werden die verschiedenen Modi von Aspose.Cells.GridWeb beschrieben. Diese Modi werden aufgrund ihrer unterschiedlichen Funktionen und Verhaltensweisen logisch voneinander abgegrenzt. Wir haben mehrere Arten von Modi identifiziert:

- Bearbeitungsmodus
- Anzeigemodus
- Sitzungsmodus
- Sitzungsloser Modus

Jeder dieser Modi hat seine eigenen Merkmale. Entwickler können mit Aspose.Cells.GridWeb in jedem Modus gemäß ihren Anforderungen arbeiten. Wir werden uns jeden Modus unten genauer ansehen.

{{% /alert %}} 
## **Bearbeitungsmodus**
Standardmäßig ist die Aspose.Cells.GridWeb-Steuerung im Bearbeitungsmodus. Im Bearbeitungsmodus können Sie den Rasterinhalt vollständig bearbeiten oder modifizieren und dabei alle Funktionen der Aspose.Cells.GridWeb-Steuerung nutzen. Zu diesen Funktionen gehören:

- Speichern des Rasterinhalts in Microsoft Excel-Dateien.
- Übermittlung von Daten an einen Server.
- Berechnung von Formeln.
- Rückgängigmachen oder Verwerfen früherer Aktionen.
- Verwalten von Zeilen und Spalten.
- Ausschneiden, Kopieren oder Einfügen von Daten.
- Formatieren von Zellen usw.

**GridWeb Steuerelement im Bearbeitungsmodus** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Entwickler können auch programmgesteuert in den Bearbeitungsmodus wechseln, indem sie die EditMode-Eigenschaft des GridWeb-Steuerelements auf true setzen.

Das folgende Beispiel zeigt, wie der Bearbeitungsmodus programmgesteuert aktiviert wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

Wenn ein Benutzer auf die Schaltfläche **Rückgängig** klickt, wird GridWeb in seinen vorherigen Zustand versetzt (den Zustand vor dem letzten Postback zum Server). Es hebt jedoch nicht vorherige Aktionen einzeln auf.

{{% /alert %}} 
## **Anzeigemodus**
Wenn die GridWeb-Steuerelement im Anzeigemodus ist, können Benutzer den Rasterinhalt nicht bearbeiten oder ändern. Das bedeutet, dass Benutzer nur den Rasterinhalt anzeigen können. Daher wird dieser Modus als Anzeigemodus bezeichnet. Im Anzeigemodus sind einige Schaltflächen (**Senden**, **Speichern** und **Rückgängig**) ausgeblendet und das erscheinende Menü bei einem Rechtsklick enthält nur die **Kopieren**-Option.

**GridWeb Steuerelement im Anzeigemodus** 

![todo:image_alt_text](enable-different-gridweb-modes_1.png)

Wenn Entwickler möchten, dass ihre Benutzer nur Daten anzeigen, können sie programmgesteuert in den Anzeigemodus wechseln, indem sie die Eigenschaft EditMode des GridWeb-Steuerelements auf false setzen.

Das folgende Beispiel zeigt, wie der Anzeigemodus programmgesteuert aktiviert wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Auch im Anzeigemodus können Benutzer die Höhe und Breite von Zeilen und Spalten ändern.

{{% /alert %}} 
## **Sitzungsmodus**
Das Aspose.Cells.GridWeb-Steuerelement speichert Blattdaten in der Benutzersitzung des Webservers zwischen jeder Anfrage eines Webbenutzers. Das bedeutet, dass das GridWeb-Steuerelement standardmäßig immer im Sitzungsmodus arbeitet. Wenn Sie jedoch nicht im Sitzungsmodus arbeiten, aktivieren Sie ihn, indem Sie die Eigenschaft SessionMode des GridWeb-Steuerelements auf SessionMode.Session setzen.

Das folgende Beispiel zeigt, wie der Sitzungsmodus programmgesteuert aktiviert wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Sitzungsloser Modus**
Wir haben bereits besprochen, dass der Session-Modus den besten Leistung durch Verwenden einer Benutzersitzung zum Laden und Speichern von Blattdaten bietet. Er verbraucht jedoch Server-Speicher. Daher können bei einer großen Anzahl gleichzeitiger Benutzer Speicherprobleme auftreten. Um Speicherspeicher zu sparen und eine große Anzahl von gleichzeitigen Benutzern zu unterstützen, sollten Sie den Sitzungslosen Modus in Betracht ziehen.

Der Sitzungslose Modus kann aktiviert werden, indem Sie die Eigenschaft SessionMode des GridWeb-Steuerelements auf SessionMode.ViewState setzen.

Das folgende Beispiel zeigt, wie der sitzungslose Modus programmgesteuert aktiviert wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Wenn die SessionMode-Eigenschaft von GridWeb auf SessionMode.ViewState festgelegt ist, speichert das Raster Daten im ViewState der Seite. Das bedeutet, dass die gerenderte Seite größer ist und mehr Netzwerkverkehr verursacht.

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Sie SQL Server oder StateServer verwenden möchten, um Sitzungen zu halten, verwenden Sie den Sessionmodus. Die GridWeb-Steuerung unterstützt das Serialisieren ihrer Daten in SQL Server oder StateServer.

Bitte überprüfen Sie den folgenden Artikel für weitere Hilfe.

- [Arbeiten von GridWeb, wenn der ASP.NET-Sitzungsstatusmodus SQL Server ist](/cells/de/net/aspose-cells-gridweb/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}

---
title: Aktivieren Sie verschiedene GridWeb-Modi
type: docs
weight: 60
url: /de/net/enable-different-gridweb-modes/
---
{{% alert color="primary" %}} 

Dieser Artikel beschreibt die verschiedenen Modi von Aspose.Cells.GridWeb. Diese Modi unterscheiden sich logisch aufgrund ihrer unterschiedlichen Merkmale und Verhaltensweisen. Wir haben mehrere Arten von Modi identifiziert:

- Bearbeitungsmodus
- Ansichtsmodus
- Sitzungsmodus
- Sitzungsloser Modus

Alle diese Modi haben ihre eigenen Eigenschaften. Entwickler können mit Aspose.Cells.GridWeb in jedem Modus entsprechend ihren Anforderungen arbeiten. Wir werden uns jeden Modus unten ansehen.

{{% /alert %}} 
## **Bearbeitungsmodus**
Standardmäßig befindet sich das Aspose.Cells.GridWeb-Steuerelement im Bearbeitungsmodus. Im Bearbeitungsmodus können Sie den Rasterinhalt vollständig bearbeiten oder ändern, indem Sie alle Funktionen verwenden, die das Steuerelement Aspose.Cells.GridWeb bietet. Zu diesen Funktionen gehören:

- Speichern des Rasterinhalts in Microsoft Excel-Dateien.
- Senden von Daten an einen Server.
- Formeln berechnen.
- Vorherige Aktionen rückgängig machen oder verwerfen.
- Zeilen und Spalten verwalten.
- Ausschneiden, Kopieren oder Einfügen von Daten.
- Zellen formatieren usw.

**GridWeb-Steuerelement im Bearbeitungsmodus** 

![todo: Bild_alt_Text](enable-different-gridweb-modes_1.png)

Entwickler können auch programmgesteuert in den Bearbeitungsmodus wechseln, indem sie die EditMode-Eigenschaft des GridWeb-Steuerelements auf true festlegen.

Das folgende Beispiel zeigt, wie der Bearbeitungsmodus programmgesteuert aktiviert wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyEditMode.cs" >}}

{{% alert color="primary" %}} 

 Immer wenn ein Benutzer auf die klickt**Rückgängig machen** Schaltfläche bringt es das GridWeb in seinen vorherigen Zustand (den Zustand vor dem letzten Postback an den Server). Vorherige Aktionen werden nicht einzeln abgebrochen.

{{% /alert %}} 
## **Ansichtsmodus**
Wenn sich das GridWeb-Steuerelement im Ansichtsmodus befindet, können Benutzer den Rasterinhalt nicht bearbeiten oder ändern, was bedeutet, dass Benutzer den Rasterinhalt nur anzeigen können. Deshalb wird dieser Modus Ansichtsmodus genannt. Im Ansichtsmodus sind einige Schaltflächen (**Einreichen**, **Speichern** und**Rückgängig machen** ) sind ausgeblendet und das Menü, das beim Rechtsklick erscheint, enthält nur die**Kopieren** Möglichkeit.

**GridWeb-Steuerelement im Ansichtsmodus** 

![todo: Bild_alt_Text](enable-different-gridweb-modes_1.png)

Wenn Entwickler möchten, dass ihre Benutzer nur Daten anzeigen, können sie programmgesteuert in den Ansichtsmodus wechseln, indem sie die EditMode-Eigenschaft des GridWeb-Steuerelements auf „false“ festlegen.

Das folgende Beispiel zeigt, wie der Ansichtsmodus programmgesteuert aktiviert wird



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyEditModes.aspx-ApplyViewMode.cs" >}}

{{% alert color="primary" %}} 

Auch im Ansichtsmodus können Benutzer die Höhe und Breite von Zeilen und Spalten ändern.

{{% /alert %}} 
## **Sitzungsmodus**
Das Aspose.Cells.GridWeb-Steuerelement hält Blattdaten in der Benutzersitzung des Webservers zwischen den einzelnen Anforderungen eines Webbenutzers. Dies bedeutet, dass die GridWeb-Steuerung standardmäßig immer im Sitzungsmodus arbeitet. Wenn Sie jedoch nicht im Sitzungsmodus arbeiten, schalten Sie ihn ein, indem Sie die SessionMode-Eigenschaft des GridWEb-Steuerelements auf SessionMode.Session festlegen.

Das folgende Beispiel zeigt, wie der Sitzungsmodus programmgesteuert aktiviert wird



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionMode.cs" >}}
## **Sitzungsloser Modus**
Wir haben bereits besprochen, dass der Ansatz im Sitzungsmodus die beste Leistung bietet, indem eine Benutzersitzung zum Laden und Speichern von Blattdaten verwendet wird. Es verbraucht jedoch Serverspeicher. Wenn also eine große Anzahl gleichzeitiger Benutzer vorhanden ist, können Speicherprobleme auftreten. Ziehen Sie den sitzungslosen Modus in Betracht, um Serverspeicher zu sparen und eine große Anzahl gleichzeitiger Benutzer zu unterstützen.

Der sitzungslose Modus kann aktiviert werden, indem die SessionMode-Eigenschaft des GridWeb-Steuerelements auf SessionMode.ViewState festgelegt wird.

Das folgende Beispiel zeigt, wie der sitzungslose Modus programmgesteuert aktiviert wird



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplySessionModes.aspx-ApplySesionlessMode.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Wenn die SessionMode-Eigenschaft von GridWeb auf SessionMode.ViewState festgelegt ist, speichert das Raster Daten im ViewState der Seite. Das bedeutet, dass die gerenderte Seite größer ist und mehr Netzwerkverkehr verbraucht.

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Sie SQL Server oder StateServer zum Abhalten von Sitzungen verwenden möchten, verwenden Sie den Sitzungsmodus. Das GridWeb-Steuerelement unterstützt die Serialisierung seiner Daten zu SQL Server oder StateServer.

Weitere Hilfe finden Sie im folgenden Artikel.

- [Funktionieren von GridWeb, wenn der ASP.NET-Sitzungsstatusmodus SQL Server ist](/cells/de/net/working-of-gridweb-when-asp-net-session-state-mode-is-sql-server/)

{{% /alert %}}

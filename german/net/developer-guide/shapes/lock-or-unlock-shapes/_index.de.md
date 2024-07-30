---
title: Formen sperren oder freigeben
linktitle: Formen sperren oder freigeben
type: docs
weight: 200
url: /de/net/lock-or-unlock-shapes/
description: Dieser Artikel zeigt Ihnen Code, der erklärt, wie Sie Formen sperren oder entsperren, um sie mit der Aspose.Cells Bibliothek zu schützen.
keywords: C# Sperrt Formen zum Schutz, Wie Sie Formen mit C# sperren oder entsperren, Formen sperren oder entsperren zum Schutz in C#.
---

## **Mögliche Verwendungsszenarien**

Manchmal müssen Sie alle Formen in bestimmten Tabellenblättern schützen, um zu verhindern, dass sie durch unerwünschte Situationen zerstört werden. In diesem Fall müssen Sie alle Formen im angegebenen Tabellenblatt sperren. 

Das Sperren von Formen in einer Tabelle oder einem Dokument kann aus mehreren Gründen vorteilhaft sein:
1. Verhindern von versehentlichen Änderungen: Das Sperren von Formen stellt sicher, dass sie nicht versehentlich von Benutzern verschoben, vergrößert oder gelöscht werden. Dies ist besonders wichtig in komplexen Dokumenten, in denen Formen für Anmerkungen, Illustrationen oder als Teil des Designs des Dokuments verwendet werden.
1. Layout und Design beibehalten: Formen spielen oft eine entscheidende Rolle im Layout und im visuellen Design eines Dokuments. Indem man sie sperrt, bleibt das beabsichtigte Erscheinungsbild erhalten und stellt sicher, dass das Dokument professionell und visuell ansprechend bleibt.
1. Datenintegrität: In Tabellen können Formen verwendet werden, um wichtige Datenpunkte hervorzuheben, Kommentare hinzuzufügen oder visuelle Erklärungen bereitzustellen. Durch das Sperren dieser Formen wird sichergestellt, dass die kontextbezogenen Informationen genau und intakt bleiben.
1. Konsistenz in gemeinsam genutzten Dokumenten: Beim gemeinsamen Bearbeiten von Dokumenten haben unterschiedliche Benutzer möglicherweise unterschiedliche Kenntnisse. Das Sperren von Formen hilft dabei, die Konsistenz im gesamten Dokument zu gewährleisten, indem unbeabsichtigte Änderungen verhindert werden.
1. Sicherheit: In sensiblen Dokumenten kann das Sperren von Formen Teil einer umfassenderen Strategie zum Schutz von Informationen sein. Beispielsweise können in Finanzberichten oder rechtlichen Dokumenten gesperrte Formen verwendet werden, um spezifische Anmerkungen oder Hervorhebungen zu schützen, die wichtige Kontextinformationen bieten.

Manchmal müssen bestimmte Formen in bestimmten geschützten Tabellenblättern geändert werden können, in diesem Fall müssen diese Formen entsperrt werden. Dieser Artikel wird detailliert erläutern, wie man bestimmte Formen sperrt und entsperrt.

## **So sperren Sie Formen, um sie in Excel zu schützen**

So können Sie Zellen in Microsoft Excel sperren:

1. Öffnen Sie Ihre Excel-Datei: Öffnen Sie die Excel-Datei, die die Formen enthält, die Sie sperren möchten.

1. Wählen Sie die Form aus: Klicken Sie auf die Form, die Sie sperren möchten. Sie können auch mehrere Formen auswählen, indem Sie die Strg-Taste gedrückt halten und auf jede Form klicken.

1. Öffnen Sie das Format-Shape-Fenster: Klicken Sie mit der rechten Maustaste auf die ausgewählte(n) Form(en) und wählen Sie "Größe und Eigenschaften." Alternativ können Sie auf dem Registerband auf die Registerkarte "Format" gehen und in der Gruppe "Größe" auf den Dialogstart (einen kleinen Pfeil) klicken, um das "Format-Shape"-Fenster zu öffnen.
1. Sperren Sie die Form: Gehen Sie im "Format-Shape"-Fenster zur Registerkarte "Größe & Eigenschaften" (das Symbol sieht wie ein Quadrat mit Pfeilen aus). Unter dem Abschnitt "Eigenschaften" aktivieren Sie das Kontrollkästchen "Gesperrt".
<br>
<img src="1.png" width=60% />
1. Schützen Sie das Arbeitsblatt: Gehen Sie zum Reiter "Überprüfen" im Menüband. Klicken Sie auf "Blatt schützen". Legen Sie ein Passwort fest (optional) und wählen Sie die Berechtigungen aus, die Sie zulassen möchten (z. B. Auswahl gesperrter Zellen, Zellen formatieren usw.). Klicken Sie auf "OK".
<br>
<img src="2.png" width=60% />

## **Wie man alle Formen in einem bestimmten Arbeitsblatt sperrt**

Um alle Formen in einem angegebenen Arbeitsblatt zu schützen, verwenden Sie die Methode [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect), wie im folgenden Beispielcode gezeigt.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Wie man bestimmte Formen in einem geschützten Tabellenblatt entriegelt**

Um eine bestimmte Form in einem geschützten Arbeitsblatt zu entsperren, verwenden Sie [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), wie im folgenden Beispielcode gezeigt.

Hinweis: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) ist nur sinnvoll, wenn das Arbeitsblatt geschützt ist.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}


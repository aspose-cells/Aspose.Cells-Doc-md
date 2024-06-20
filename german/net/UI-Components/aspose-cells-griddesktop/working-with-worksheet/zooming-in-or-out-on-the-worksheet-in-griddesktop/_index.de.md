---
title: Hinein oder Hinauszoomen auf dem Arbeitsblatt in GridDesktop
type: docs
weight: 160
url: /de/net/aspose-cells-griddesktop/zoom-in-or-out-on-the-worksheet-in-griddesktop/
keywords: GridDesktop, zoomen, hineinzoomen, hinauszoomen
description: Dieser Artikel zeigt, wie man in GridDesktop hineinzoomen oder hinauszoomen kann.
---

{{% alert color="primary" %}} 

Manchmal möchten Sie beim Arbeiten mit Ihren Daten die Inhalte auf dem Bildschirm vergrößern, ohne die Schriftgröße tatsächlich zu ändern. Sie haben möglicherweise Ihren Text formatiert, damit er eine kleine Schriftart verwendet. (Das ist oft notwendig, um alle Ihre Informationen auf einem Ausdruck zu platzieren.) Beim Arbeiten im Arbeitsblatt ist die Schrift aber schwer lesbar, weil sie so klein ist.

In Microsoft Excel ist ein Zoomregler zum schnellen und einfachen Vergrößern und Verkleinern von Dokumenten verfügbar. Der Zoomregler befindet sich normalerweise in der unteren rechten Ecke des Softwarefensters.

Aspose.Cells ermöglicht es Entwicklern auch, den Zoomfaktor des Arbeitsblatts festzulegen, sodass die Inhalte gemäß des gewünschten Prozentwerts erscheinen sollen.

{{% /alert %}} 
## **Ein- oder Auszoomen mit Aspose.Cells.GridDesktop**
Aspose.Cells bietet die Aspose.Cells.GridDesktop.Worksheet-Klasse, die eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern enthält. Verwenden Sie die Zoom-Eigenschaft der Worksheet-Klasse, um den Zoomfaktor eines Arbeitsblatts festzulegen. Der Zoomfaktor wird durch die Zuweisung eines numerischen (ganzzahligen) Werts an die Zoom-Eigenschaft festgelegt.

Wir erstellen einen MS Excel-ähnlichen Zoomregler unter Verwendung des TrackBar (.NET)-Steuerelements. In einem WinForm-Projekt platzieren wir das Aspose.Cells.GridDesktop-Steuerelement aus der Toolbox auf dem Formular und geben einige Eigenschaften an, um seinen Namen, seine Größe oder andere Aspekte entsprechend festzulegen. Nun platzieren wir das TrackBar-Steuerelement in der unteren rechten Ecke unterhalb des GridDesktop-Steuerelements und fügen auch ein Label-Steuerelement hinzu, das den prozentualen Wert anzeigen soll, den Sie über das TrackBar-Steuerelement festlegen. Wir fügen relative Codezeilen im Scroll-Ereignis des TrackBar hinzu, sodass beim Scrollen des TrackBar-Steuerelements der GridDesktop herein- oder herauszoomen sollte, um die Daten/Inhalte darin anzuzeigen.

Im folgenden Beispiel wird gezeigt, wie man die Zoom-Eigenschaft verwendet, um den Zoomfaktor des aktiven Arbeitsblatts von GridDesktop festzulegen. Zuerst importieren wir eine Vorlagen-Excel-Datei in GridDesktop.

Schreiben Sie den untenstehenden Code im Load-Ereignis des Formulars, um die Vorlagen-Excel-Datei in GridDesktop und den Trackbar-Wert festzulegen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Kopieren Sie nun den untenstehenden Code in das Scroll-Ereignis des Tracks und führen Sie die Anwendung aus. Sie werden feststellen, dass sich beim Verschieben des Trackbar der Zoomwert des Arbeitsblatts ändert.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}

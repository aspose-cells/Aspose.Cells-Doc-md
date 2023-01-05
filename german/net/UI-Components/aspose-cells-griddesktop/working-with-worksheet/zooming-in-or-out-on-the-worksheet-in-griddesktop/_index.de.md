---
title: Vergrößern oder Verkleinern des Arbeitsblatts in GridDesktop
type: docs
weight: 160
url: /de/net/zooming-in-or-out-on-the-worksheet-in-griddesktop/
---
{{% alert color="primary" %}} 

Wenn Sie mit Ihren Daten arbeiten, möchten Sie möglicherweise manchmal den Inhalt auf dem Bildschirm vergrößern, ohne die Schriftgröße tatsächlich zu ändern. Möglicherweise haben Sie Ihren Text beispielsweise so formatiert, dass er eine kleine Schriftart verwendet. (Dies ist oft notwendig, um alle Informationen auf einem Ausdruck zu erhalten.) Beim Arbeiten im Arbeitsblatt ist die Schrift jedoch aufgrund der geringen Größe schwer lesbar.

In Microsoft Excel steht ein Zoom-Schieberegler zum schnellen und einfachen Vergrößern und Verkleinern von Dokumenten zur Verfügung. Der Zoom-Schieberegler befindet sich normalerweise in der unteren rechten Ecke des Softwarefensters.

Aspose.Cells ermöglicht es Entwicklern auch, den Zoomfaktor des Arbeitsblatts festzulegen, sodass der Inhalt gemäß Ihrem gewünschten Prozentwert angezeigt werden sollte.

{{% /alert %}} 
## **Vergrößern oder verkleinern mit Aspose.Cells.GridDesktop**
Aspose.Cells stellt die Klasse Aspose.Cells.GridDesktop.Worksheet bereit, die eine Vielzahl von Eigenschaften und Methoden zum Verwalten von Arbeitsblättern aufweist. Um den Zoomfaktor eines Arbeitsblatts festzulegen, verwenden Sie die Zoom-Eigenschaft der Worksheet-Klasse. Der Zoomfaktor wird festgelegt, indem der Zoom-Eigenschaft ein numerischer (ganzzahliger) Wert zugewiesen wird.

Wir erstellen einen MS Excel-ähnlichen Zoom-Schieberegler mit TrackBar (.NET)-Steuerung. In einem WinForm-Projekt platzieren wir das Aspose.Cells.GridDesktop-Steuerelement aus der Toolbox im Formular und geben einige Eigenschaften an, um seinen Namen, seine Größe oder andere Aspekte entsprechend festzulegen. Jetzt platzieren wir das TrackBar-Steuerelement @ untere rechte Ecke unter dem GridDesktop-Steuerelement. Außerdem platzieren wir ein Label-Steuerelement, das den Prozentwert anzeigt, den Sie über das Handle des TrackBar-Steuerelements angeben. Wir fügen relative Codezeilen in das Scroll-Ereignis von TrackBar ein, sodass GridDesktop beim Scrollen des Trackbar-Steuerelements hinein- oder herauszoomen sollte, um die darin enthaltenen Daten/Inhalte anzuzeigen.

Nachfolgend finden Sie ein vollständiges Beispiel, das zeigt, wie Sie die Zoom-Eigenschaft verwenden, um den Zoomfaktor des aktiven Arbeitsblatts von GridDesktop festzulegen. Wir importieren zunächst eine Excel-Vorlagendatei in GridDesktop.

Schreiben Sie den folgenden Code in das Load-Ereignis des Formulars, um die Excel-Vorlagendatei in GridDesktop und den Trackbar-Wert festzulegen.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-LoadEvent.cs" >}}


Kopieren Sie nun den folgenden Code in das Track-Scroll-Ereignis und führen Sie die Anwendung aus. Sie werden feststellen, dass das Bewegen der Spurleiste die Zoom-Eigenschaft des Arbeitsblatts ändert.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ZoomingInOut-ZoomInOut.cs" >}}

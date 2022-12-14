---
title: Öffnen einer Excel-Datei ohne Dialogfeld „Speichern/Abbrechen öffnen“.
type: docs
weight: 150
url: /de/net/opening-excel-file-without-open-save-cancel-dialog-box/
---
{{% alert color="primary" %}} 

In diesem Dokument wird erläutert, wie Sie eine Microsoft-Excel-Datei in einem Browser öffnen, ohne das Dialogfeld Öffnen-Speichern-Abbrechen anzuzeigen.

 Hier ist zu beachten, dass die Sicherheitsbeschränkung, die das direkte Herunterladen einer Datei nicht zulässt, von Microsoft (oder anderen Browseranbietern) durchgesetzt wird, nicht von Aspose. Sie wird auferlegt, um potenziell schädliche Dateien daran zu hindern, auf lokale Computer heruntergeladen zu werden .

Es ist riskant, dass das lokale System des Clients den Download zulässt, ohne dass das Dialogfeld „Öffnen – Speichern – Abbrechen“ angezeigt wird, um zum Herunterladen aufzufordern. Unter Aspose ist keine Option oder Problemumgehung verfügbar, da dies ein sehr großes Sicherheitsrisiko darstellt.

{{% /alert %}} 
## **Warum ein Sicherheitsrisiko?**
Die folgende Abbildung zeigt das Dialogfeld Öffnen-Speichern-Abbrechen, das von Internet Explorer angezeigt wird, wenn versucht wird, eine Datei herunterzuladen.

|**Der Dialog Öffnen-Speichern-Abbrechen**|
|:- |
|![todo: Bild_alt_Text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
Wie oben erläutert, ist das Öffnen oder Ausführen einer Datei auf Ihrem System ohne Bestätigung, dass Sie dies wirklich wollen, ein Sicherheitsrisiko. Einige Dateien enthalten Viren, und einige Websites versuchen, schädliche Dateien auf Ihren Computer herunterzuladen, ohne Sie dazu aufzufordern. Es wird daher nicht empfohlen, das Herunterladen von Dateien ohne die Aufforderung zum Herunterladen zuzulassen, damit Benutzer die Datei überprüfen müssen und ihre Quelle überprüft werden kann, bevor sie heruntergeladen oder ausgeführt wird. Das Deaktivieren des Download-Dialogfelds macht das System anfällig für Viren, Trojaner und Hacker, die Ihr System unbemerkt beeinflussen können.
## **Öffnen einer Datei ohne das Dialogfeld Öffnen-Speichern-Abbrechen**
 Obwohl es ein großes Sicherheitsproblem darstellt, bietet Microsoft immer noch Internet Explorer-Einstellungen, die es Benutzern ermöglichen, die Open-Save-Cancel-Aufforderung für den Dateidownload zu deaktivieren.

In Windows Entdecker:

1.  Auf der**Werkzeug** Menü, auswählen**Ordneroptionen**.
1. Klicken Sie im Dialogfeld Ordneroptionen auf die Registerkarte Dateitypen.
1. Wählen Sie den Dateityp XLS-Erweiterung aus.
1.  Klicken**Fortschrittlich**. 
Ein Dialogfeld wird angezeigt. Es hat unten drei Optionen.
1.  Deaktivieren**Bestätigen Sie das Öffnen nach dem Download**.
1.  Wählen Sie die dritte Option -**Durchsuchen Sie im selben Fenster** - um die Excel-Datei im Internet Explorer anzuzeigen, ohne Microsoft Excel Standalone zu starten.

|**Dateitypoptionen bearbeiten**|
|:- |
|![todo: Bild_alt_Text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
Mit dieser Einstellung können Dateien direkt im Webbrowser ausgeführt werden, ohne dass beim Herunterladen oder Öffnen der Datei der Dialog Öffnen-Speichern-Abbrechen angezeigt wird.

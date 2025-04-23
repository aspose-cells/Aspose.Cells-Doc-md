---
title: Öffnen einer Excel Datei ohne Dialogfeld Öffnen Speichern Abbrechen
type: docs
weight: 150
url: /de/net/opening-excel-file-without-open-save-cancel-dialog-box/
---

{{% alert color="primary" %}} 

Dieses Dokument erklärt, wie man eine Microsoft Excel-Datei im Browser öffnet, ohne das Dialogfeld Öffnen-Speichern-Abbrechen anzuzeigen. 

Es ist hier zu beachten, dass die Sicherheitsbeschränkung, die das direkte Herunterladen einer Datei verhindert, von Microsoft (oder anderen Browser-Anbietern) durchgesetzt wird, nicht von Aspose. Sie wird eingeführt, um potenziell schädliche Dateien daran zu hindern, auf lokale Maschinen heruntergeladen zu werden. 

Es ist riskant für das lokale System des Clients, den Download ohne das Dialogfeld Öffnen-Speichern-Abbrechen zu ermöglichen, um den Download aufzufordern. Es gibt keine Option oder Lösung von Aspose, da dies ein sehr großes Sicherheitsrisiko darstellen würde.

{{% /alert %}} 
## **Warum ein Sicherheitsrisiko?**
Das folgende Bild zeigt das Dialogfeld Öffnen-Speichern-Abbrechen, das von Internet Explorer angezeigt wird, wenn versucht wird, eine Datei herunterzuladen.

|**Das Dialogfeld Öffnen-Speichern-Abbrechen**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_1.png)|
Wie oben erklärt, birgt es ein Sicherheitsrisiko, eine Datei auf Ihrem System zu öffnen oder auszuführen, ohne die Bestätigung, dass Sie es wirklich möchten. Einige Dateien enthalten Viren, und einige Websites werden versuchen, schädliche Dateien auf Ihren Rechner herunterzuladen, ohne Sie zu fragen. Es wird daher nicht empfohlen, den Dateidownload ohne die Download-Aufforderung zuzulassen, damit Benutzer die Datei überprüfen und deren Quelle verifiziert werden kann, bevor sie sie herunterladen oder ausführen. Das Deaktivieren des Download-Dialogfelds macht das System anfällig für Viren, Trojaner und Hacker, die Ihr System möglicherweise heimlich beeinflussen. 
## **Öffnen einer Datei ohne das Dialogfeld Öffnen-Speichern-Abbrechen**
Obwohl es ein großes Sicherheitsproblem ist, bietet Microsoft immer noch Internet Explorer-Einstellungen, die es den Benutzern ermöglichen, die Dialogfeld-Öffnen-Speichern-Abbrechen-Prompt für den Dateidownload zu deaktivieren. 

Im Windows Explorer:

1. Wählen Sie im **Extras**-Menü **Ordneroptionen**.
1. Klicken Sie im Dialogfeld Ordneroptionen auf die Registerkarte Dateitypen.
1. Wählen Sie den Dateityp mit der XLS-Erweiterung aus.
1. Klicken Sie auf **Erweitert**. 
   Ein Dialogfeld wird angezeigt. Es hat drei Optionen unten.
1. Deaktivieren Sie die Option **Bestätigen Sie nach dem Download das Öffnen**.
1. Wählen Sie die dritte Option - **Im gleichen Fenster durchsuchen** - um die Excel-Datei in Internet Explorer anzuzeigen, ohne Microsoft Excel eigenständig zu starten. 

|**Optionen zum Bearbeiten des Dateityps**|
| :- |
|![todo:image_alt_text](opening-excel-file-without-open-save-cancel-dialog-box_2.png)|
Mit dieser Einstellung können Dateien direkt im Webbrowser ausgeführt werden, ohne dass beim Herunterladen oder Öffnen der Datei der Dialog zum Öffnen-Speichern-Abbrechen angezeigt wird.
{{< app/cells/assistant language="csharp" >}}

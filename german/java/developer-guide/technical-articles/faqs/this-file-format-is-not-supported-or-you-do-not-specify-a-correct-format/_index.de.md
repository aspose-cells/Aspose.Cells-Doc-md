---
title: Dieses Dateiformat wird nicht unterstützt oder Sie haben kein korrektes Format angegeben
type: docs
weight: 10
url: /de/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **Dieses Dateiformat wird nicht unterstützt oder Sie haben kein korrektes Format angegeben**
Wenn der Benutzer das Dateiformat beim Erstellen der Arbeitsmappe aus einer Vorlage angegeben hat, liegt dieser Fehler häufig daran, dass das angegebene Dateiformat nicht dem tatsächlichen Dateiformat der Vorlage entspricht. Wenn der Benutzer das Dateiformat nicht angegeben hat, liegt es häufig daran, dass die Dateierweiterung den tatsächlichen Dateityp nicht repräsentiert und das Dateiformat nicht automatisch erkannt werden kann, z.B. bei der csv/tsv-Datei, die keine besonderen Kennzeichen hat. Natürlich melden auch nicht unterstützte Dateiformate durch Cells diesen Fehler.
{{< app/cells/assistant language="java" >}}

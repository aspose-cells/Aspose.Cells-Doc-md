---
title: Dokument nicht gespeichert Problem
type: docs
weight: 40
url: /de/net/document-not-saved-issue/
---

## **Problem**
Ich habe ein seltsames Problem mit einem Spreadsheet, das ich mit Ihrer Steuerung erstellt habe. Es öffnet und bearbeitet sich gut in Excel, aber wenn ich versuche, zu speichern oder speichern unter durchzuführen, erhalte ich eine "Dokument nicht gespeichert"-Meldung.
### **Problemzusammenfassung**
Dies ist ein Excel-Bug: 

"Dokument nicht gespeichert" Speichern von einer Vorlagendatei erstellte Datei

Artikel-ID: 121942

Letzte Überprüfung: 15. August 2005

Revision: 1.3

Dieser Artikel wurde zuvor unter Q121942 veröffentlicht
### **Symptom**
Beim Versuch, eine Arbeitsmappe zu speichern, erhalten Sie möglicherweise folgende Fehlermeldung: **"Dokument nicht gespeichert"**
### **Ursachen**
Dieses Problem kann auftreten, wenn die folgenden Bedingungen erfüllt sind:

- Die Arbeitsmappe wurde aus einer Vorlage erstellt, die ein eingebettetes Objekt enthielt.
- Sie haben ein Arbeitsblatt aus einer Vorlage in Ihre Arbeitsmappe eingefügt.
- Die Vorlage enthält ein eingebettetes Objekt.
### **Lösung**
Um Ihre Arbeit zu speichern, müssen Sie zuerst die eingebetteten Objekte in Ihrer Arbeitsmappe löschen.

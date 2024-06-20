---
title: Dokumentet inte sparat problem
type: docs
weight: 40
url: /sv/net/document-not-saved-issue/
---

## **Problem**
Jag har ett märkligt problem med ett kalkylark jag skapat med din kontroll. Det öppnas och redigeras fint i Excel, men när jag försöker spara eller spara som, får jag en "Dokument inte sparat" msgbox.
### **Problem Sammanfattning**
Detta är en Excel-bugg: 

"Dokumentet inte sparat" Sparande av fil skapad från mall

Artikel-ID : 121942

Senast granskad : 15 augusti, 2005

Revision : 1.3

Den här artikeln tidigare publicerats under Q121942
### **Symptom**
När du försöker spara en arbetsbok kan du få följande felmeddelande: **"Dokumentet inte sparat"**
### **Orsaker**
Detta problem kan uppstå när följande villkor är sanna:

- Arbetsboken skapades från en mall som innehöll en inbäddad objekt.
- Du har infogat en kalkylblad i din arbetsbok från en mall.
- Mallen innehåller en inbäddad objekt.
### **Lösning**
För att spara ditt arbete måste du först ta bort de inbäddade objekten i din arbetsbok.

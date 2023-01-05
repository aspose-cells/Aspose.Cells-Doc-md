---
title: Dokument inte sparat ärende
type: docs
weight: 40
url: /sv/net/document-not-saved-issue/
---
## **Problem**
Jag har ett konstigt problem med ett kalkylblad som jag har skapat med din kontroll. Den öppnas och redigeras helt okej i Excel, men när jag försöker utföra en Spara eller Spara som får jag ett meddelande om "Dokument inte sparat".
### **Sammanfattning av problem**
 Detta är en Excel-bugg:

"Dokument inte sparat" Sparar fil skapad från mall

Artikel-id: 121942

Senaste recension: 15 augusti 2005

Revision: 1.3

Den här artikeln har tidigare publicerats under Q121942
### **Symptom**
 När du försöker spara en arbetsbok kan du få följande felmeddelande:**"Dokument inte sparat"**
### **Orsaker**
Det här problemet kan uppstå när följande villkor är uppfyllda:

- Arbetsboken skapades från en mall som innehöll ett inbäddat objekt.
- Du har infogat ett kalkylblad i din arbetsbok från en mall.
- Mallen innehåller ett inbäddat objekt.
### **Lösning**
För att spara ditt arbete måste du först ta bort de inbäddade objekten i din arbetsbok.

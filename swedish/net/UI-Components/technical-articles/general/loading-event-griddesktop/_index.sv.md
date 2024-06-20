---
title: Inläsningshändelse i GridDesktop
type: docs
weight: 1060
url: /sv/net/aspose-cells-griddesktop/loading-event
description: Denna artikel beskriver hur man använder laddningsevenemang i GridDesktop.
keywords: GridDesktop,event,laddningsevenemang,laddning
---


## **Laddningsevenemang för GridDesktop**
Följande exempelkod illustrerar hur man använder typer av laddningsevenemang för GridDesktop vid import av en fil. Vänligen kontrollera [provexcelfilen](loading-event.xlsx) . 

Filen är lösenordsskyddad, först försöker vi öppna den med ett fel lösenord, och slutligen i FailLoadFile-evenemanget använder vi ett korrekt lösenord för att öppna den.

![resultatvy för laddningsevenemang](loadingevent.png)
### **Exempelkod**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "LoadingEvent.cs" >}}


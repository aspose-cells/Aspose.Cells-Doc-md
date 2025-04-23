---
title: Versionshantering
type: docs
weight: 40
url: /sv/go-cpp/versioning/
description: Hur man installerar Aspose Cells for Go via C++ och skapar ett Hello World program.
---

**github.com/aspose-cells/aspose-cells-go-cpp/v25** är en Go-modulsökväg som specificerar en viss version av ett tredjepartsbibliotek. Låt oss bryta ner denna sökväg och förklara dess betydelse:
Bryta ner modulsökvägen

1. **GitHub-repositorieadress**: github.com/aspose-cells/aspose-cells-go-cpp

- Denna del visar att biblioteket är hostat på GitHub, under organisationen eller användaren aspose-cells, i repositoriet som heter aspose-cells-go-cpp.
- Aspose.Cells är en svit av API:er för att hantera och manipulera kalkylbladsfiler (som Excel).

1. **Versionsnummer**: /v25

- /v25 indikerar att detta är version 25 av biblioteket. I Go-moduler stöds semantisk versionering (SemVer), där sökvägar som innehåller /vN används för att explicit specificera huvudversionen.
- När huvudversionen är större än eller lika med 2 måste modulsökvägen inkludera versionsnumret för att säkerställa kompatibilitet och isolering mellan olika huvudversioner.

### **Betydelse**

- **aspose-cells-go-cpp**: Detta är en Go-språkbindning för ett C++-bibliotek, som gör det möjligt att använda Aspose.Cells funktionaliteter i dina Go-program för att läsa, skriva och manipulera Excel-filer, bland andra operationer.
- **v25**: Detta indikerar att du hänvisar till version 25 av biblioteket. Olika huvudversioner kan introduce inkompatibla förändringar, så att specificera versionsnumret är avgörande för att din projekt ska bero på rätt API och beteende.

### **Användning**

För att använda aspose-cells-go-cpp v25 i ditt Go-projekt, måste du lägga till följande rad i din go.mod-fil:

```Go
require github.com/aspose-cells/aspose-cells-go-cpp/v25 v25.x.x
```

Byt ut v25.x.x mot det specifika minor- och patchversionsnumret, exempelvis v25.0.0. Du kan automatiskt lägga till och ladda ner detta beroende med kommandot go get:

```Go
go get github.com/aspose-cells/aspose-cells-go-cpp/v25@v25.x.x
```

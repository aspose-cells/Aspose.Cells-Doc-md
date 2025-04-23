---
title: Säkerhetsundantagsproblem
type: docs
weight: 30
url: /sv/net/security-exception-issue/
---

## **Säkerhetsundantagsproblem**
Vissa användare kan få "Säkerhetsundantags" felmeddelande när de försöker använda Aspose.Cells. Detta problem inträffar vanligtvis i en webbapplikation.
### **Förklaring**
Aspose.Cells måste anropa vissa **Win32 GDI APIs** för att tillhandahålla vissa viktiga funktioner. Om webbservern har en strikt förtroendenivå kan detta säkerhetsundantag kastas.
### **Lösning**
Försök skapa en ny behörighetsuppsättning för att ge Aspose.Cells.dll säkerhetsbehörighet med "Tillåt anrop till hanterade föreningar" aktiverat.
{{< app/cells/assistant language="csharp" >}}

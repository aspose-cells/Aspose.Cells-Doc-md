---
title: Säkerhetsundantagsproblem
type: docs
weight: 30
url: /sv/net/security-exception-issue/
---
## **Problem med säkerhetsundantag**
Vissa användare kan få felmeddelandet "Säkerhetsundantag" när de försöker använda Aspose.Cells. Detta problem uppstår vanligtvis i en webbapplikation.
### **Förklaring**
 Aspose.Cells måste ringa några**Win32 GDI API:er** för att tillhandahålla några viktiga funktioner. Om webbservern har en strikt förtroendenivå kan detta säkerhetsundantag kastas.
### **Lösning**
Försök att skapa en ny behörighetsuppsättning för att ge Aspose.Cells.dll säkerhetsbehörighet med "Tillåt anrop till ohanterade sammanställningar" aktiverat.

---
title: Detta filformat stöds inte eller så har du inte angett rätt format
type: docs
weight: 10
url: /sv/java/this-file-format-is-not-supported-or-you-do-not-specify-a-correct-format/
---

## **Detta filformat stöds inte eller så har du inte angett ett korrekt format**
 Om användaren har specificerat filformatet vid skapandet av arbetsboken från mallfilen, är detta fel ofta eftersom det angivna filformatet inte är det faktiska filformatet för mallfilen. Om användaren inte har angett filformatet, beror det oftast på att filnamnstillägget inte representerar det faktiska filformatet för denna fil och filformatet kan inte upptäckas automatiskt, exempelvis csv/tsv-filer som inte har några särskilda identifierare. Naturligtvis kommer även filformat som inte stöds av Cells att rapportera detta fel.
{{< app/cells/assistant language="java" >}}

---
title: Aspose.Cells för Java 16.10.0 Release Notes
type: docs
weight: 30
url: /sv/java/aspose-cells-for-java-16-10-0-release-notes/
---
## **1) Aspose.Cells**

|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-41974 | Uppdatering av pivottabell fungerar inte i den renderade PDF-filen| Insekt|
|CELLSJAVA-41900 | XLSM blir skadad av enkel laddning och lagring| Insekt|
|CELLSJAVA-41790 | Hyperlänkar fungerar inte som förväntat efter konvertering av kalkylblad till HTML| Insekt|
|CELLSJAVA-42010 | Vissa tecken återges inte i utdata-PDF-filen| Insekt|
|CELLSJAVA-41977 | Ordningen på sjökortsförklaringen har ändrats i diagrammets PDF| Insekt|
|CELLSJAVA-41972 | Z-ordningen av hög-låg rader är inte korrekt i PDF| Insekt|
|CELLSJAVA-42015 | Kalkylarket blir skadat efter att ha sparats på nytt med Aspose.Cells| Insekt|
|CELLSJAVA-42005 | Formeln ändras efter infogning i en cell| Insekt|
|CELLSJAVA-41997 | Konstigt beteende med enkla bönor med Smart Markers| Insekt|
|CELLSJAVA-41993 | NullPointerException när du öppnar filen a7.xlsm| Undantag|
|CELLSJAVA-41992 | NullPointerException när du öppnar filen a6.xlsm| Undantag|
|CELLSJAVA-41991 |NullPointerException när du öppnar filen a5.xlsm| Undantag|
|CELLSJAVA-41990 | NullPointerException när du öppnar filen a4.xlsm| Undantag|
|CELLSJAVA-41989 | NullPointerException när du öppnar filen a3.xlsm| Undantag|
|CELLSJAVA-41988 | NullPointerException när du öppnar filen a2.xlsm| Undantag|
|CELLSJAVA-41987 | NullPointerException när du öppnar filen a1.xlsm| Undantag|
|CELLSJAVA-41968 | IndexOutOfBoundsException: Index: 23, Storlek: 14 medan pivotdiagram uppdateras| Undantag|
|CELLSJAVA-42014 | ClassCastException: com.aspose.cells.zadp kan inte castas till com.aspose.cells.zadq medan XLSX sparas på nytt| Undantag|
## **Public API och bakåtinkompatibla ändringar**
Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.
### **Lägger till egenskapen Shape.Reflection och klassen ReflectionEffect**
Representerar reflektionseffekt för diagramelementet eller formen.
### **Lägger till egenskaperna Shape.Glow, GlowEffect.Size och GlowEffect.Transparency**
Representerar glödeffekt för diagramelementet eller formen.
### **Lägger till LightRigType.None enum**
Representerar ingen ljusinställning.
### **Lägger till egenskapen Shape.ShadowEffect**
Representerar skuggeffekt för diagramelementet eller formen.
### **Lägger till egenskapen ExternalLink.IsVisible**
Indikerar om den externa länken är synlig.
### **Lägger till egenskapen Shape.ThreeDFormat och klassen ThreeDFormat**
Hämtar och ställer in 3d-format av formen.
### **Lägger till PresetCameraType enum**
Representerar olika algoritmiska metoder för att ställa in alla kameraegenskaper, inklusive position.
### **Lägger till LightRigDirectionType enum**
Representerar typen av ljusriggriktning.
### **Lägger till BevelType enum**
Representerar en förinställning för en typ av fas som kan appliceras på en form i 3D.
### **Lägger till metoden XmlMapCollection.Add(string url).**
Lägger till en XmlMap genom url/sökväg till en XML-fil.
### **Lägger till metoden ShapeCollection.AddWordArt() och PresetWordArtStyle enum**
Lägger till förinställd WordArt sedan MS Excel 2007.
### **Lägger till metoden FontSettingCollection.SetWordArtStyle() och metoden FontSetting.SetWordArtStyle()**
Ställer in förinställd WordArt-stil till formens text.
### **Lägger till metoden Cells.LinkToXmlMap(string mapName, int rad, int kolumn, sträng sökväg)**
Länk till en xml-karta.
### **Lägger till egenskapen ListColumn.Formula**
Hämtar och ställer in formeln för listkolumnen.
### **Lägger till GridWeb.CustomCalculationEngine-egenskapen och GridAbstractCalculationEngine-klassen**
Representerar användarens anpassade beräkningsmotor för att utöka standardberäkningsmotorn för Aspose.Cells.GridWeb.

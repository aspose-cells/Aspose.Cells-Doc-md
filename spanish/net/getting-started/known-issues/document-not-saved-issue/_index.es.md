---
title: Problema de Documento no guardado 
type: docs
weight: 40
url: /es/net/document-not-saved-issue/
---

## **Problema**
Estoy teniendo un problema extraño con una hoja de cálculo que he creado con su control. Abre y edita perfectamente en Excel, pero cuando intento guardar o guardar como, recibo un mensaje de error "Documento no guardado".
### **Resumen del problema**
Este es un error de Excel: 

"Documento no guardado" Al guardar archivo creado a partir de plantilla

ID del artículo: 121942

Última Revisión: 15 de agosto de 2005

Revisión : 1.3

Este artículo fue publicado anteriormente bajo Q121942
### **Síntoma**
Cuando intentas guardar un libro de trabajo, es posible que recibas el siguiente mensaje de error: **"Documento no guardado"**
### **Causas**
Este problema puede ocurrir cuando se cumplen las siguientes condiciones:

- El libro de trabajo se creó a partir de una plantilla que contenía un objeto incrustado.
- Has insertado una hoja de cálculo en tu libro de trabajo desde una plantilla.
- La plantilla contiene un objeto incrustado.
### **Solución**
Para guardar tu trabajo, primero debes eliminar los objetos incrustados en tu libro de trabajo.

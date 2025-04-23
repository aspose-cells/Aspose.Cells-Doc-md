---
title: Problema de Excepción de Seguridad
type: docs
weight: 30
url: /es/net/security-exception-issue/
---

## **Problema de Excepción de Seguridad**
Algunos usuarios pueden recibir el error "Excepción de Seguridad" al intentar usar Aspose.Cells. Este problema generalmente ocurre en una aplicación web.
### **Explicación**
Aspose.Cells debe llamar a algunas API **Win32 GDI** para proporcionar algunas características importantes. Si el servidor web tiene un nivel de confianza estricto, esta excepción de seguridad puede ser lanzada.
### **Solución**
Por favor, intente crear un nuevo conjunto de permisos para otorgar a Aspose.Cells.dll permiso de seguridad con "Permitir llamadas a ensamblajes no administrados" habilitado.
{{< app/cells/assistant language="csharp" >}}

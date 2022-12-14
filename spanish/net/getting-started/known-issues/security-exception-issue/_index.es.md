---
title: Problema de excepción de seguridad
type: docs
weight: 30
url: /es/net/security-exception-issue/
---
## **Problema de excepción de seguridad**
Algunos usuarios pueden recibir el error "Excepción de seguridad" al intentar usar Aspose.Cells. Este problema generalmente ocurre en una aplicación web.
### **Explicación**
 Aspose.Cells tiene que llamar a algunos**API Win32 GDI** para proporcionar algunas características importantes. Si el servidor web tiene un nivel de confianza estricto, es posible que se produzca esta excepción de seguridad.
### **Solución**
Intente crear un nuevo conjunto de permisos para otorgar el permiso de seguridad Aspose.Cells.dll con "Permitir llamadas a ensamblados no administrados" habilitado.

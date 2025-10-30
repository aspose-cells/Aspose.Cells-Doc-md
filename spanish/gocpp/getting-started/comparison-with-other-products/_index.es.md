---
title: Comparación de funcionalidad y rendimiento de Aspose.Cells para Go a través de C con Excelize, Tealeg/xlsx, y Go OLE.
linktitle: Comparación de funcionalidad y rendimiento
type: docs
weight: 40
url: /es/go-cpp/comparison-of-functionality-and-performance/
description: Comparación de funcionalidad y rendimiento de Aspose.Cells para Go a través de C con Excelize, Tealeg/xlsx, y Go OLE.
keywords: Aspose.Cells, Excel, Ventana de Observación de Fórmulas, Celdas, Agregar, C++
---

Lo siguiente es una comparación exhaustiva de Aspose.Cells para Go (a través de C) con otras bibliotecas principales de procesamiento de Excel en lenguaje Go (Excelize, tealeg/xlsx, go-ole) en términos de funcionalidad, rendimiento y casos de uso.

## Diferencias en posicionamiento y estructura básicas

| Nombre de la biblioteca |   Tipo                      | Implementación subyacente | Dependencia de CGO | Implementación multiplataforma |
| :------------------- | :----------------------------- | :--------------------------------- | :----------------------- | :-----------------------  |
| Aspose.Cells para Go  | Biblioteca Comercial (MIT/Paga) | Motor nativo, Wrapper de CGO en Go |  ✅  Sí | Soporte para Windows, Linux |
| Excelize             | Biblioteca de código abierto (MIT) | Implementación pura en Go |  ❌  No | Soporte para Windows, Linux, MacOS |
| tealeg/xlsx          | Biblioteca de código abierto (BSD) | Implementación pura en Go |  ❌  No | Soporte para Windows, Linux, MacOS |
| go-ole               | Biblioteca de código abierto (BSD) | Interfaz OLE/COM de Windows en Go |  ✅  Sí (solo Windows) | Solo Windows |

### Diferencias clave

- Aspose.Cells for Go via C++ es una biblioteca de grado industrial con funciones completas, pero requiere un producto de pago.
- Excelize es actualmente la biblioteca de Go activa y de código abierto, pura en Go.
- Tealeg/xlsx es una biblioteca de código abierto temprana con funciones más básicas y mantenimiento lento.
- Go-ole es un esquema de automatización COM solo para Windows que depende de la instalación de Excel y no se recomienda para entornos de servidor.

## Comparación de Características

### Comparación de Formatos de Archivo Soportados

| Formato de Hoja de Cálculo |   Aspose.Cells for Go via C++ | Excelize    | Tealeg/xlsx | Go-OLE (Aplicación Excel) |
| :--------------------- | :---------------------------- | :---------- | :---------- | :-------------------  |
| Xlsx                   | ✅ Sí                        | ✅ Sí     | ✅ Sí       | ✅ Dependiente de Excel |
| Xlsb                   | ✅ Sí                        | ❌ No     | ❌ No       | ✅ Dependiente de Excel |
| Xls                    | ✅ Sí                        | ❌ No     | ❌ No       | ✅ Dependiente de Excel |
| Xlsm                   | ✅ Sí                        | ✅ Sí     | ✅ Sí       | ✅ Dependiente de Excel |
| Xltm                   | ✅ Sí                        | ✅ Sí     | ✅ Sí       | ✅ Dependiente de Excel |
| Xltx                   | ✅ Sí                        | ✅ Sí     | ✅ Sí       | ✅ Dependiente de Excel |
| Csv                    | ✅ Sí                        | ❌ No     | ❌ No       | ✅ Dependiente de Excel |
| Ods                    | ✅ Sí                        | ❌ No     | ❌ No       | ✅ Dependiente de Excel |
| Html                   | ✅ Sí                        | ❌ No     | ❌ No       | ❌ No             |
| Números                | ✅ Sí                        | ❌ No     | ❌ No       | ❌ No             |
| Json                   | ✅ Sí                        | ❌ No     | ❌ No       | ❌ No             |
| Xml                    | ✅ Sí                        | ❌ No     | ❌ No       | ❌ No             |
| SpreadsheetML          | ✅ Sí                        | ❌ No     | ❌ No       | ❌ No             |

### Características Soportadas de la Hoja de Cálculo

| Características de la Biblioteca    |   Aspose.Cells for Go via C++ | Excelize         | Tealeg/xlsx | Go-OLE (Aplicación Excel) |
| :----------------------------    | :---------------------------- | :--------------- | :---------- | :----------  |
| Leer/Escribir (Soporta formato de archivo) | ✅ Sí                        | ✅ Sí          | ✅ Sí     | ✅ Sí   |
| Celda/Fila/Columna/Hoja             | ✅ Sí                        | ✅ Sí          | ✅ Sí     | ✅ Sí   |
| Estilo                            | ✅ Sí                        | ✅ Sí          | ✅ Sí     | ✅ Sí   |
| Cálculo de fórmula              | ✅ Sí                        | ✅ Sí (Parcial)   | ❌  No     | ✅ Sí (calculado por Excel)  |
| Gráfico/Imagen                    | ✅ Sí                        | ✅ Sí (Parcial)   | ❌  No     | ✅ Sí   |
| Tabla dinámica                       | ✅ Sí                        | ✅ Sí          | ❌  No     | ✅ Sí   |
| Formato condicional           | ✅ Sí                        | ✅ Sí          | ❌  No     | ✅ Sí   |
| Validación de datos                  | ✅ Sí                        | ✅ Sí          | ❌  No     | ✅ Sí   |
| Encriptación/protección con contraseña   | ✅ Sí                        | ✅ Sí          | ❌  No     | ✅ Sí   |
| Validación de datos                  | ✅ Sí                        | ✅ Sí          | ❌  No     | ✅ Sí   |
| Macro VBA                        | ✅ Sí Leer                   | ❌  No          | ❌  No     | ✅ Sí   |
| Validación de datos                  | ✅ Sí                        | ✅ Sí          | ❌  No     | ✅ Sí   |

## Comparación de rendimiento

- **Entorno de prueba**：
Procesador: Intel(R) Core(TM) i7-12700 de 12ª generación (2.10 GHz)
RAM instalada: 64,0 GB (63,7 GB utilizables)
Nombre del SO: Microsoft Windows 11 Pro
Versión del SO: 10.0.26100
Arquitectura del SO: 64 bits
Versión de Go: go version go1.24.5 windows/amd64
Aspose.Cells for Go via C++: 25.9.0
Excelize: 1.4.1

- **Escenario de prueba**: suponiendo un archivo grande, 10 hojas de cálculo, 100,000 filas x 250 columnas, incluyendo formato.

- **Resultados de ejecución**:
  - Excelize se ejecuta durante 35 minutos (Hora de inicio: 2025-10-09T10:04:16+08:00, Hora de fin: 2025-10-09T10:39:53+08:00), tamaño del archivo generado: 1.11 GB.
  - Aspose.Cells for Go via C++ (modelo 1) se ejecuta durante 27 minutos (Hora de inicio: 2025-10-09T10:57:55+08:00, Hora de fin: 2025-10-09T11:16:24+08:00), tamaño del archivo generado: 936 MB.
  - Aspose.Cells for Go via C++ (modelo 2) se ejecuta durante 16 minutos (Hora de inicio: 2025-10-09T12:01:26+08:00, Hora de fin: 2025-10-09T12:17:17+08:00), tamaño del archivo generado: 1.16 GB.

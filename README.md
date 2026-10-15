# Sistema de Gestión de Inventario y Ventas para Colmado

## Objetivo
Automatizar el control de inventario, las ventas y los reportes básicos de un colmado, reduciendo los errores de registro manual y las pérdidas por falta de control de existencias.

## Problema que resuelve
Los colmados suelen llevar el inventario y las ventas en cuadernos o de memoria. Esto produce diferencias de existencias, productos agotados o vencidos sin aviso y poca visibilidad sobre las ganancias reales del negocio.

## Funcionalidades principales
- Registro y consulta de productos, categorías y proveedores
- Control de existencias con alerta de stock mínimo
- Registro de ventas y generación de comprobantes
- Registro de compras y entradas de mercancía
- Reportes de ventas e inventario
- Gestión de usuarios y roles (administrador y cajero)

## Arquitectura seleccionada
Arquitectura cliente-servidor en tres capas: presentación, lógica de negocio y acceso a datos. La separación permite modificar la interfaz sin alterar las reglas del negocio y facilita el mantenimiento y las pruebas.

## Herramientas utilizadas
- GitHub: repositorio, Issues y GitHub Projects
- Markdown y Mermaid: documentación y modelos UML
- HTML, CSS y JavaScript: interfaz web
- API REST con intercambio de datos en JSON
- Base de datos relacional

## Estado actual
Fases de análisis y diseño completadas. La documentación técnica y el control de versiones están al día (versión `v0.1.0`). La implementación de los módulos está pendiente.

## Organización frontend y backend

**Frontend.** Se encarga de la interfaz de usuario: formularios de productos y ventas, consulta de inventario, reportes y validaciones básicas de entrada. No contiene reglas de negocio; captura datos, los envía al servidor y presenta las respuestas.

**Backend.** Se encarga de la lógica de negocio y de los datos: validación de reglas (por ejemplo, impedir una venta sin existencias suficientes), actualización del inventario, autenticación y control de roles, y persistencia en la base de datos.

**Comunicación.** El frontend se comunica con el backend mediante una API REST sobre HTTP, con datos en formato JSON. Al registrar una venta, el frontend envía una petición `POST /ventas`; el backend valida los datos, descuenta las existencias, guarda la transacción y devuelve la confirmación o el error correspondiente.

## Documentación
- [Requisitos](requisitos.md)
- [Modelos UML](modelos-uml.md)
- [Arquitectura](arquitectura.md)
- [Gestión del avance y riesgos](gestion-avance.md)
- [Registro de cambios](CHANGELOG.md)
- [Nota técnica de versión](nota-version-v0.1.0.md)

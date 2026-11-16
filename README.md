# 🧪 QA Automation: Selenium WebDriver + Python & Pytest

Repositorio dedicado a la práctica y desarrollo de pruebas automatizadas de interfaz de usuario (UI) para aplicaciones web, utilizando **Python**, **Selenium WebDriver** y **Pytest** en **PyCharm** como framework de ejecución.

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python 3.11.5
* **Automatización Web:** Selenium WebDriver
* **Framework de Pruebas:** Pytest (`pytest-html` para reportes)
* **IDE:** PyCharm
* **Sitios de Práctica:** Automation Exercise, Test Automation Practice

## 📚 Temas y Ejercicios Cubiertos
- [x] Configuración de entorno virtual (`.venv`) y Pytest en PyCharm
- [ ] Localizadores básicos (`ID`, `Name`, `Class Name`)
- [ ] Localizadores avanzados (`XPath`, `CSS Selector`)
- [ ] Manejo de esperas explícitas (`WebDriverWait` y `Expected Conditions`)
- [ ] Interacción con `iframes` y elementos interceptados (JavaScript Executor)
- [ ] Aserciones (`assert`) y validación de resultados
- [ ] Patrón de diseño Page Object Model (POM)
- [ ] Integración de reportes y notificaciones (Slack / HTML)

## 🚀 Listos para ejecutar las pruebas localmente

1. Clona este repositorio:
   ```bash
   git clone https://github.com
   ```
2. Crea y activa tu entorno virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   ```
3. Instala las dependencias:
   ```bash
   pip install selenium pytest
   ```
4. Ejecuta la suite de pruebas:
   ```bash
   pytest -v
   ```

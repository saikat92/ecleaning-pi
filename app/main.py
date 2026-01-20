
# ================================
# main.py
# Entry point for E-Cleaning Raspberry Pi Application
# ================================

import time
from core.state_manager import StateManager
from core.logger import get_logger

logger = get_logger()


def main():
    logger.info("E-Cleaning system starting...")

    state_manager = StateManager()

    try:
        while True:
            state_manager.run()
            time.sleep(0.1)
    except KeyboardInterrupt:
        logger.warning("System interrupted manually")
    except Exception as e:
        logger.error(f"Critical system error: {e}")
    finally:
        state_manager.shutdown()
        logger.info("System shutdown completed")


if __name__ == "__main__":
    main()


import time
import pyautogui


def keep_task_running(minutes):
  """
  keep the task running and make sure the laptop no go into the inactive
  :param minutes: the minutes to finish the task
  :return:
  """
  running_interval = 60 * 10
  total_iterations = int(minutes * 60 / running_interval)  # keep the task run every 10 minutes
  print(f"keep the task running for {minutes} minutes ({total_iterations} iterations).")

  for i in range(total_iterations):
    print(f"running iteration {i + 1}/{total_iterations}...")
    pyautogui.moveRel(0, 1, duration=0.1)
    pyautogui.moveRel(0, -1, duration=0.1)
    time.sleep(running_interval)  # wait for 10 minutes

if __name__ == "__main__":
  keep_task_running(4 * 60)

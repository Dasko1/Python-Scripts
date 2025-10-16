from win10toast import ToastNotifier # type: ignore

# create an object to ToastNotifier class
n = ToastNotifier()

n.show_toast("GEEKSFORGEEKS!", "Here is the toast notification text!", duration = 5);
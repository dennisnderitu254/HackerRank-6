;;(defun fn (n)
;;    (_________________)

;;(fn (read))
    
(setq strN (read-line))
(setq N (parse-integer strN))
(loop for i from 1 to N do
    (princ "Hello World")
    (terpri)
)
